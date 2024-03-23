import streamlit as st

# CSS
header_css = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Ubuntu:ital,wght@0,300;0,400;0,500;0,700;1,300;1,400;1,500;1,700&display=swap');

.header {
    background-color: red;
    color: white;
    padding: 10px 40px;
    font-size: 24px;
    font-family: 'Ubuntu', cursive; /* Use the font */
}

/* Ensure the entire column is clickable if needed and styled correctly */
.header-container {
    width: 100%;
    background-color: red;
}

.fileUploader {
    border: 2px solid #e6e6e6;
    border-radius: 5px;
    padding: 20px;
    width: 100%;
    margin-bottom: 20px;
}

.fileUploader label {
    color: black;
    background-color: red;
    padding: 10px 20px;
    border-radius: 5px;
    font-family: sans-serif;
    margin-left: 10px;
    margin-top: 10px;
}

/* Style the button to match your theme */
.fileUploader div {
    background-color: red;
    color: white;
    border-radius: 5px;
    font-family: sans-serif;
}

/* Change button hover effect */
.fileUploader div:hover {
    background-color: #ff4d4d; /* Lighten red on hover */
}

</style>
"""

st.markdown(header_css, unsafe_allow_html=True)

st.markdown("<div class='header-container'><div class='header'>ApexAI</div></div>", unsafe_allow_html=True)

st.title("ApexAI")

st.write("Explore the thrilling world of racing. Dive into live simulations and much more.")

tab1, tab2, tab3 = st.tabs(["Home", "Race Mode", "Make a racetrack"])
tab1.write("Home")
tab2.write("Race Mode")



with tab2:
    st.radio('Select one:', ["Weather", "Track"])

with tab3:
    st.markdown('<div class="fileUploader">', unsafe_allow_html=True)
    uploaded_file = st.file_uploader("Upload your racetrack image", type=["jpg", "jpeg", "png"], key="file_uploader")
    st.markdown('</div>', unsafe_allow_html=True)

# Do something with the uploaded file
    if uploaded_file is not None:
    # To read file as bytes:
        bytes_data = uploaded_file.getvalue()
        st.write("Image uploaded successfully!")

    # To display the uploaded image:
        st.image(uploaded_file, caption='Uploaded Racetrack.', use_column_width=True)
# un comment and merge!!!
# import streamlit as st
# from cars import cars  # Assuming cars.py contains the cars list

# # Placeholder for the function that sends data to your Pygame AI model
# def send_to_pygame_ai(car_data):
#     # Simulate sending data to the Pygame AI model
#     # You'll need to replace this with actual code that integrates with your model
#     st.success(f"Sending to Pygame AI: {car_data}")

# def main():
#     st.title("Car Specifications")

#     # Create a list of car names for the dropdown menu
#     car_names = [car["name"] for car in cars]

#     # Let the user select a car name from the dropdown
#     selected_car_name = st.selectbox("Select a car", car_names)

#     # Find the selected car in the cars list
#     selected_car = next(car for car in cars if car["name"] == selected_car_name)

#     if selected_car:
#         col1, col2 = st.columns([2, 3])  # Adjust the ratio to your preference

#         with col1:
#             specifications = selected_car["specifications"]

#             st.subheader(selected_car["name"])
#             st.write(f"**Type:** {selected_car['type']}")
#             st.write("**Specifications:**")
#             spec_table = selected_car["specifications"]
#             for spec_key, spec_value in spec_table.items():
#                 st.write(f"**{spec_key.replace('_', ' ').capitalize()}:** {spec_value}")
        
#         with col2:
#             # Display the car image in a larger size within the second column
#             if 'image_url' in selected_car and selected_car["image_url"]:
#                 st.image(selected_car["image_url"], use_column_width=True, caption=selected_car["name"])

#         # Button to select the car and send data
#             if st.button("Select Car"):
#                 car_data = {
#                     "maxSpeed": specifications.get('maxSpeed'),
#                     "horsepower": specifications.get('horsepower'),
#                     "downforce": specifications.get('downforce')
#                 }
#                 send_to_pygame_ai(car_data)

# if __name__ == "__main__":
#     main()

# cars.py
# import json

# cars = [
#     {
#     "name": "F1 Redbull Car",
#     "type": "Racing",
#     "specifications": {
#         "horsepower": 1000,
#         "downforce": 0.95,
#         "maxSpeed": 230,
#         "engine_type": "1.6L V6 turbo hybrid",
#         "torque": 500,
#         "braking_hp": 300, 
#         "transmission": "8-speed semi-automatic",
#         "suspension": "Carbon-fiber double wishbone with springs and anti-roll bar"
#         },
#         "image_url": "https://www.acfligue.org/wp-content/uploads/2023/02/custom_showroom_1677516834.png"
#     },
#     {
#         "name": "NASCAR Car",
#         "type": "Racing",
#         "specifications": {
#             "horsepower": 850,
#             "downforce": 0.7,
#             "maxSpeed": 200,
#             "engine_type": "V8",
#             "torque": 650,
#             "transmission": "4-speed manual",
#             "suspension": "Independent coil springs"
#         },
#         "image_url": "https://hips.hearstapps.com/hmg-prod/images/c0115dde9d3c069a5c9641932d1635b9.png"
#     },
#     {
#         "name": "Le Mans Car",
#         "type": "Racing",
#         "specifications": {
#             "horsepower": 900,
#             "downforce": 0.85,
#             "maxSpeed": 210,
#             "engine_type": "Turbocharged V6",
#             "torque": 720,
#             "transmission": "6-speed sequential",
#             "suspension": "Double wishbone"
#         },
#         "image_url": "https://bammotorsportmanagement.com/wp-content/uploads/2020/09/Transparent-Nielsen_Oreca_LMP2_V3_Front-970x546.png"
#     },
#     {
#         "name": "Toyota Camry",
#         "type": "Normal",
#         "specifications": {
#             "horsepower": 300,
#             "downforce": 0.3,
#             "maxSpeed": 130,
#             "engine_type": "V6",
#             "torque": 267,
#             "transmission": "8-speed automatic",
#             "suspension": "MacPherson strut"
#         },
#         "image_url": "https://www.cars.com/i/large/in/v2/stock_photos/2edb1b06-b6a3-4b2d-b7ce-f8f005335ba2/79b3ed52-ea96-43cf-8b1f-7fcd29e20f24.png"
#     },
#     {
#         "name": "Honda Civic",
#         "type": "Normal",
#         "specifications": {
#             "horsepower": 158,
#             "downforce": 0.25,
#             "maxSpeed": 125,
#             "engine_type": "Inline-4",
#             "torque": 138,
#             "transmission": "CVT automatic",
#             "suspension": "Multi-link"
#         },
#         "image_url": "https://automobiles.honda.com/-/media/Honda-Automobiles/Vehicles/2024/civic-sedan/AW/Carshot/carshot_CivicSedan_front_CIVIC20L4DSPORT_2024_AegeanBlueMetallic_FE2F5REW_B-593M.png"
#     },
#     {
#         "name": "Ford Fiesta",
#         "type": "Normal",
#         "specifications": {
#             "horsepower": 120,
#             "downforce": 0.2,
#             "maxSpeed": 112,
#             "engine_type": "Inline-4",
#             "torque": 112,
#             "transmission": "5-speed manual",
#             "suspension": "Twist-beam"
#         },
#         "image_url": "https://assets-clean.local-car-finder.com/images/13069/13069_st1280_089.png"
#     },
#     {
#         "name": "Volkswagen Golf",
#         "type": "Normal",
#         "specifications": {
#             "horsepower": 147,
#             "downforce": 0.28,
#             "maxSpeed": 127,
#             "engine_type": "Turbocharged Inline-4",
#             "torque": 184,
#             "transmission": "7-speed automatic",
#             "suspension": "Independent"
#         },
#         "image_url": "https://content-images.carmax.com/stockimages/2020/volkswagen/golf/st2400-089-evoxwebmedium.png"
#     },
#     {
#         "name": "Chevrolet Malibu",
#         "type": "Normal",
#         "specifications": {
#             "horsepower": 160,
#             "downforce": 0.27,
#             "maxSpeed": 130,
#             "engine_type": "Turbocharged Inline-4",
#             "torque": 184,
#             "transmission": "CVT automatic",
#             "suspension": "MacPherson strut front, multi-link rear"
#         },
#         "image_url": "https://www.motortrend.com/uploads/sites/10/2018/11/2019-chevrolet-malibu-lt-sedan-angular-front.png?fit=around%7C551:374"
#     },
#     {
#         "name": "Subaru Impreza",
#         "type": "Normal",
#         "specifications": {
#             "horsepower": 152,
#             "downforce": 0.26,
#             "maxSpeed": 140,
#             "engine_type": "Boxer-4",
#             "torque": 145,
#             "transmission": "5-speed manual",
#             "suspension": "Independent"
#         },
#         "image_url": "https://www.cars.com/i/large/in/v2/stock_photos/7a0eaf27-b3d6-4806-a3ee-82aa3925e962/0f606829-a3db-49cd-8605-17b6a7110eef.png"
#     },
#     {
#         "name": "Mazda 3",
#         "type": "Normal",
#         "specifications": {
#             "horsepower": 186,
#             "downforce": 0.29,
#             "maxSpeed": 135,
#             "engine_type": "Inline-4",
#             "torque": 186,
#             "transmission": "6-speed automatic",
#             "suspension": "MacPherson strut"
#         },
#         "image_url": "https://www.mazdausa.com/siteassets/vehicles/2024/mazda3-sedan/build-and-price/trims/34-jellies/preferred/fwd/2024-mazda-3-sedan-2.5-s-preferred-package"
#     }
# ]
