import pygame
import os
import math
import sys
import random
import neat
from pymongo import MongoClient

MONGO_URI = "mongodb+srv://nihal41:Nihal2004!@cluster0.jumqmmz.mongodb.net/"
DATABASE_NAME = "formula"
client = MongoClient(MONGO_URI)
db = client[DATABASE_NAME]

screen_width = 1500
screen_height = 800
generation = 0
best_overall_lap_time = 1000  # Assuming 1000 is a placeholder for a very high initial value
unchanged_generations = 0  # Counter for generations without improvement
max_overall_reward = 0
best_net = 0
done_training = False
best_car = 0
line = []
SCALE = 0.4
car_file_name = ""


time_cutoff = 1000
specs = {}


def find_average_green_pixel_position(surface):
    total_x, total_y, green_count = 0, 0, 0
    width, height = surface.get_size()
    for x in range(width):
        for y in range(height):
            color = surface.get_at((x, y))
            if color.g > 2 * color.r and color.g >  2* color.b:
                total_x += x
                total_y += y
                green_count += 1
    if green_count == 0:
        return None
    average_x = total_x // green_count
    average_y = total_y // green_count
    return [average_x, average_y]


avg_start_pixel = [0,0]




class Car:
    def __init__(self, map):
        self.best_lap_time = 1000
        self.lap_completed = False
        self.lap_start_time = 0
        self.lap_time = 0
        self.surface = pygame.image.load(car_file_name)
        self.surface = pygame.transform.scale(self.surface, (100 * SCALE, 100 * SCALE))
        self.rotate_surface = self.surface
        self.pos = [avg_start_pixel[0] - 50 * SCALE, avg_start_pixel[1] - 50 * SCALE]
        self.angle = 0
        self.speed = max_speed
        self.center = [self.pos[0] + 50 * SCALE, self.pos[1] + 50 * SCALE]
        self.radars = []
        self.radars_for_draw = []
        self.is_alive = True
        self.goal = False
        self.distance = 0
        self.time_spent = 0

    def draw(self, screen):
        screen.blit(self.rotate_surface, self.pos)
        # self.draw_radar(screen)

    def draw_radar(self, screen):
        for r in self.radars:
            pos, dist = r
            pygame.draw.line(screen, (0, 255, 0), self.center, pos, 1)
            pygame.draw.circle(screen, (0, 255, 0), pos, 5)

    
    def check_collision(self, map):
        self.is_alive = True
        for p in self.four_points:
            if map.get_at((int(p[0]), int(p[1]))) == (255, 255, 255, 255):
                self.is_alive = False
                break

    def check_radar(self, degree, map):
        len = 0
        x = int(self.center[0] + math.cos(math.radians(360 - (self.angle + degree))) * len)
        y = int(self.center[1] + math.sin(math.radians(360 - (self.angle + degree))) * len)

        while not map.get_at((x, y)) == (255, 255, 255, 255) and len < 300:
            len = len + 1
            x = int(self.center[0] + math.cos(math.radians(360 - (self.angle + degree))) * len)
            y = int(self.center[1] + math.sin(math.radians(360 - (self.angle + degree))) * len)

        dist = int(math.sqrt(math.pow(x - self.center[0], 2) + math.pow(y - self.center[1], 2)))
        self.radars.append([(x, y), dist])

    def update(self, map):
        #check speed

        #check position
        self.rotate_surface = self.rot_center(self.surface, self.angle)
        self.pos[0] += math.cos(math.radians(360 - self.angle)) * self.speed
        # if self.pos[0] < 20:
        #     self.pos[0] = 20
        # elif self.pos[0] > screen_width - 120:
        #     self.pos[0] = screen_width - 120

        self.distance += self.speed
        self.time_spent += 1
           
        self.pos[1] += math.sin(math.radians(360 - self.angle)) * self.speed
        # if self.pos[1] < 20:
        #     self.pos[1] = 20
        # elif self.pos[1] > screen_height - 120:
        #     self.pos[1] = screen_height - 120

        # caculate 4 collision points
        self.center = [int(self.pos[0]) + 50 * SCALE, int(self.pos[1]) + 50 * SCALE]
        len = 40 * SCALE
        left_top = [self.center[0] + math.cos(math.radians(360 - (self.angle + 30))) * len, self.center[1] + math.sin(math.radians(360 - (self.angle + 30))) * len]
        right_top = [self.center[0] + math.cos(math.radians(360 - (self.angle + 150))) * len, self.center[1] + math.sin(math.radians(360 - (self.angle + 150))) * len]
        left_bottom = [self.center[0] + math.cos(math.radians(360 - (self.angle + 210))) * len, self.center[1] + math.sin(math.radians(360 - (self.angle + 210))) * len]
        right_bottom = [self.center[0] + math.cos(math.radians(360 - (self.angle + 330))) * len, self.center[1] + math.sin(math.radians(360 - (self.angle + 330))) * len]
        self.four_points = [left_top, right_top, left_bottom, right_bottom]

        self.check_collision(map)
        if (self.time_spent > time_cutoff):
            self.is_alive = False
        if (self.speed < 1):
            self.is_alive = False
             
        self.radars.clear()
        for d in range(-90, 120, 45):
            self.check_radar(d, map)

    def get_data(self):
        radars = self.radars
        ret = [0, 0, 0, 0, 0]
        for i, r in enumerate(radars):
            ret[i] = int(r[1] / 30)

        return ret

    def get_alive(self):
        return self.is_alive

    def is_finish_line_color(self, color):
        """
        Check if the given color is a finish line color.
        - A light color (not white) or black.
        """
        # Check for black or light color (excluding pure white)
        return color == (0, 255, 0, 255)

    def check_lap_completion(self, map):
        global time_cutoff
        """
        Check if the car has completed a lap by detecting specific colors at certain points around its center.
        Record the lap time only if the car is moving forwards and the lap time is more than 5 time units.
        """
        around_center = [(int(self.center[0] + dx), int(self.center[1] + dy)) for dx in (-10, 0, 10) for dy in (-10, 0, 10)]
        
        for point in around_center:
            try:
                if self.is_finish_line_color(map.get_at(point)):
                    # Check if the car is facing backwards using its angle attribute
                    if 90 < self.angle % 360 < 100:
                        # Car is moving backwards, do not record the lap time
                        self.is_alive = False
                        return False
                    else:
                        # Car is moving forwards, check the lap time
                        current_time = self.time_spent
                        potential_lap_time = current_time - self.lap_start_time
                        if potential_lap_time > 200:  # Only record if the lap time is more than 5 time units
                            self.lap_time = potential_lap_time
                            if(self.lap_time < self.best_lap_time):
                                self.best_lap_time = self.lap_time
                            print(f"Lap completed in {self.lap_time} time units.")
                            time_cutoff = min(time_cutoff, 1.5 * self.best_lap_time)
                            self.lap_start_time = current_time  # Reset lap start time for the next lap
                            return True
                        else:
                            # Lap time is too short, do not record
                            return False
            except IndexError:
                # Handle cases where the point is outside the map bounds
                continue
        return False





    def get_reward(self):
        add_reward = 0
        add_reward = 1000 - self.best_lap_time
        if (add_reward == 0): 
            add_reward = self.distance/12.0

        # print("add rewrod: " + str(add_reward))
        # print("distance: " + str(self.distance))
        # print("total weight:" + str(self.distance/30 + add_reward))
        return add_reward
    
        

    def rot_center(self, image, angle):
        orig_rect = image.get_rect()
        rot_image = pygame.transform.rotate(image, angle)
        rot_rect = orig_rect.copy()
        rot_rect.center = rot_image.get_rect().center
        rot_image = rot_image.subsurface(rot_rect).copy()
        return rot_image
def adjust_speed_by_downforce(original_speed_change, downforce):
    # Higher downforce, less reduction
    scale_factor = ((downforce - 0.2) / (0.95 - 0.2)) * .04 + .94
    return scale_factor

def calculate_speed_increase_factor(horsepower):
    # Calculate the speed increase factor based on horsepower
    return (horsepower - 100) / 2250 + 1.01

def run_car(genomes, config):

    global best_overall_lap_time, unchanged_generations, generation, done_training, best_net, max_overall_reward, best_car, line
    # Init NEAT
    nets = []
    cars = []

    

    for id, g in genomes:
        net = neat.nn.FeedForwardNetwork.create(g, config)
        nets.append(net)
        g.fitness = 0

        # Init my cars
        cars.append(Car(map))

    # Init my game
    pygame.init()
    screen = pygame.display.set_mode((screen_width, screen_height))
    clock = pygame.time.Clock()
    generation_font = pygame.font.SysFont("Arial", 70)
    font = pygame.font.SysFont("Arial", 30)
    timer = 0


    # Main loop
    generation += 1
    didGenChange = False
    while True:
        timer += 1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)

        if(not done_training):
            # Input my data and get result from network
            for index, car in enumerate(cars):
                output = nets[index].activate(car.get_data())
                i = output.index(max(output))
                low_multi = adjust_speed_by_downforce(1, downforce)
                
                if i == 0:
                    car.angle += 20
                    car.speed *= low_multi
                elif i == 1:
                    car.angle += 15
                    car.speed *= (2 + low_multi) / 3.0
                elif i == 2:
                    car.angle += 10
                elif i == 3:
                    car.angle += 0
                    # For acceleration, adjust speed based on horsepower
                    speed_change = calculate_speed_increase_factor(horsepower)
                    if car.speed * speed_change > max_speed:
                        car.speed = max_speed
                    else:
                        car.speed *= speed_change
                    # print("Max Speed: " + str(max_speed))
                    # print(car.speed)
                elif i == 4:
                    car.angle -= 10
                elif i == 5:
                    car.angle -= 15
                    car.speed *= (2 + low_multi) / 3.0
                else:  # Assuming this is for i == 6 or any other case
                    car.angle -= 20
                    car.speed *= low_multi

            # Update car and fitness
            remain_cars = 0
            for i, car in enumerate(cars):
                if car.get_alive():
                    remain_cars += 1
                    car.update(map)
                    
                
                        # Here you can handle events upon lap completion, if needed
                    car.check_lap_completion(map)
                    genomes[i][1].fitness += car.get_reward()
                    if(genomes[i][1].fitness > max_overall_reward):
                        max_overall_reward = genomes[i][1].fitness
                        best_net = nets[i]
                        didGenChange = True
            
                


            # check
            if remain_cars == 0:
                if(not didGenChange and generation > 20):
                    unchanged_generations += 1
                    print(f"this has been the #{unchanged_generations} unchanged generation.")
                    if(unchanged_generations == 8):
                        done_training = True
                        timer = 0
                        best_car = Car(map)
                        
                else:
                    unchanged_generations = 0
                break
        
            screen.blit(map, (0, 0))
            for car in cars:
                if car.get_alive():
                    car.draw(screen)

            text = generation_font.render("Generation : " + str(generation), True, (255, 0, 0))
            text_rect = text.get_rect()
            text_rect.center = (5 + text_rect.width/2, screen_height - text_rect.height/2 - 5)
            screen.blit(text, text_rect)

            text = font.render("Remaining Cars : " + str(remain_cars), True, (0, 0, 0))
            text_rect = text.get_rect()
            text_rect.center = (screen_width - text_rect.width/2 - 5, screen_height - text_rect.height/2 - 5)
            screen.blit(text, text_rect)
            pygame.display.flip()
            clock.tick(60)
        else:

            
            if best_car and best_car.get_alive():
                screen.blit(map, (0, 0))
                output = best_net.activate(best_car.get_data())
                i = output.index(max(output))
                low_multi = adjust_speed_by_downforce(1, downforce)
                
                if i == 0:
                    best_car.angle += 20
                    best_car.speed *= low_multi
                elif i == 1:
                    best_car.angle += 15
                    best_car.speed *= (2 + low_multi) / 3.0
                elif i == 2:
                    best_car.angle += 10
                elif i == 3:
                    best_car.angle += 0
                    # For acceleration, adjust speed based on horsepower
                    speed_change = calculate_speed_increase_factor(horsepower)
                    if best_car.speed * speed_change > max_speed:
                        best_car.speed = max_speed
                    else:
                        best_car.speed *= speed_change
                elif i == 4:
                    best_car.angle -= 10
                elif i == 5:
                    best_car.angle -= 15
                    best_car.speed *= (2 + low_multi) / 3.0
                else:  # Assuming this is for i == 6 or any other case
                    best_car.angle -= 20
                    best_car.speed *= low_multi
                best_car.update(map)
                import copy
                line.append(copy.deepcopy(best_car.center))
                for i in range(len(line) - 1):
                    poi1 = line[i]
                    poi2 = line[i + 1]
                    # pygame.draw.line(screen, (255, 0, 0), poi1, poi2, 5)
                    pygame.draw.circle(screen, (255, 0, 0), poi1, 5)
                best_car.draw(screen)
            pygame.display.flip()
            clock.tick(60)


        

if __name__ == "__main__":
    collection = db['cars']  # Replace 'your_collection_name' with the actual name of your collection

    # Attempt to retrieve the single document in the collection
    car_document = collection.find_one()

    # Check if a document was found
    if car_document:
        # Print the name and specifications
        print("Name:", car_document['name'])
        if(car_document['name'] == "F1 Redbull Car"):
            car_file_name = "redbull.png"
        else:
            car_file_name = "car.png"
        print("Type:", car_document['type'])
        print("Specifications:")
        for spec, value in car_document['specifications'].items():
            print(f"  {spec}: {value}")
            if(spec == "horsepower"):
                horsepower = value
            if(spec == "downforce"):
                downforce = value
            if(spec == "maxSpeed"):
                dbspeed = value
                max_speed = 30 * dbspeed/230 * SCALE
                # max_speed = value
    else:
        print("No car found in the database.")
    collection = db['tracks']
    track_document = collection.find_one()
    if track_document:
        track_name = track_document['name']
        map = pygame.image.load(f'{track_name}.png')
        avg_start_pixel = find_average_green_pixel_position(map)

        
    # Set configuration file
    config_path = "./config-feedforward.txt"
    config = neat.config.Config(neat.DefaultGenome, neat.DefaultReproduction,
                                neat.DefaultSpeciesSet, neat.DefaultStagnation, config_path)

    # Create core evolution algorithm class
    p = neat.Population(config)

    # Add reporter for fancy statistical result
    p.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    p.add_reporter(stats)

    # Run NEAT
    p.run(run_car, 1000)