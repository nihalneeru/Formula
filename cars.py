import json

cars = [
    {
    "name": "F1 Redbull Car",
    "type": "Racing",
    "specifications": {
        "horsepower": 1000,
        "downforce": 0.95,
        "maxSpeed": 230,
        "engine_type": "1.6L V6 turbo hybrid",
        "torque": 500,
        "braking_hp": 300, 
        "transmission": "8-speed semi-automatic",
        "suspension": "Carbon-fiber double wishbone with springs and anti-roll bar"
        },
        "image_url": "https://www.acfligue.org/wp-content/uploads/2023/02/custom_showroom_1677516834.png"
    },
    {
        "name": "NASCAR Car",
        "type": "Racing",
        "specifications": {
            "horsepower": 850,
            "downforce": 0.7,
            "maxSpeed": 200,
            "engine_type": "V8",
            "torque": 650,
            "transmission": "4-speed manual",
            "suspension": "Independent coil springs"
        },
        "image_url": "https://hips.hearstapps.com/hmg-prod/images/c0115dde9d3c069a5c9641932d1635b9.png"
    },
    {
        "name": "Le Mans Car",
        "type": "Racing",
        "specifications": {
            "horsepower": 900,
            "downforce": 0.85,
            "maxSpeed": 210,
            "engine_type": "Turbocharged V6",
            "torque": 720,
            "transmission": "6-speed sequential",
            "suspension": "Double wishbone"
        },
        "image_url": "https://bammotorsportmanagement.com/wp-content/uploads/2020/09/Transparent-Nielsen_Oreca_LMP2_V3_Front-970x546.png"
    },
    {
        "name": "Toyota Camry",
        "type": "Normal",
        "specifications": {
            "horsepower": 300,
            "downforce": 0.3,
            "maxSpeed": 130,
            "engine_type": "V6",
            "torque": 267,
            "transmission": "8-speed automatic",
            "suspension": "MacPherson strut"
        },
        "image_url": "https://www.cars.com/i/large/in/v2/stock_photos/2edb1b06-b6a3-4b2d-b7ce-f8f005335ba2/79b3ed52-ea96-43cf-8b1f-7fcd29e20f24.png"
    },
    {
        "name": "Honda Civic",
        "type": "Normal",
        "specifications": {
            "horsepower": 158,
            "downforce": 0.25,
            "maxSpeed": 125,
            "engine_type": "Inline-4",
            "torque": 138,
            "transmission": "CVT automatic",
            "suspension": "Multi-link"
        },
        "image_url": "https://automobiles.honda.com/-/media/Honda-Automobiles/Vehicles/2024/civic-sedan/AW/Carshot/carshot_CivicSedan_front_CIVIC20L4DSPORT_2024_AegeanBlueMetallic_FE2F5REW_B-593M.png"
    },
    {
        "name": "Ford Fiesta",
        "type": "Normal",
        "specifications": {
            "horsepower": 120,
            "downforce": 0.2,
            "maxSpeed": 112,
            "engine_type": "Inline-4",
            "torque": 112,
            "transmission": "5-speed manual",
            "suspension": "Twist-beam"
        },
        "image_url": "https://assets-clean.local-car-finder.com/images/13069/13069_st1280_089.png"
    },
    {
        "name": "Volkswagen Golf",
        "type": "Normal",
        "specifications": {
            "horsepower": 147,
            "downforce": 0.28,
            "maxSpeed": 127,
            "engine_type": "Turbocharged Inline-4",
            "torque": 184,
            "transmission": "7-speed automatic",
            "suspension": "Independent"
        },
        "image_url": "https://content-images.carmax.com/stockimages/2020/volkswagen/golf/st2400-089-evoxwebmedium.png"
    },
    {
        "name": "Chevrolet Malibu",
        "type": "Normal",
        "specifications": {
            "horsepower": 160,
            "downforce": 0.27,
            "maxSpeed": 130,
            "engine_type": "Turbocharged Inline-4",
            "torque": 184,
            "transmission": "CVT automatic",
            "suspension": "MacPherson strut front, multi-link rear"
        },
        "image_url": "https://www.motortrend.com/uploads/sites/10/2018/11/2019-chevrolet-malibu-lt-sedan-angular-front.png?fit=around%7C551:374"
    },
    {
        "name": "Subaru Impreza",
        "type": "Normal",
        "specifications": {
            "horsepower": 152,
            "downforce": 0.26,
            "maxSpeed": 140,
            "engine_type": "Boxer-4",
            "torque": 145,
            "transmission": "5-speed manual",
            "suspension": "Independent"
        },
        "image_url": "https://www.cars.com/i/large/in/v2/stock_photos/7a0eaf27-b3d6-4806-a3ee-82aa3925e962/0f606829-a3db-49cd-8605-17b6a7110eef.png"
    },
    {
        "name": "Mazda 3",
        "type": "Normal",
        "specifications": {
            "horsepower": 186,
            "downforce": 0.29,
            "maxSpeed": 135,
            "engine_type": "Inline-4",
            "torque": 186,
            "transmission": "6-speed automatic",
            "suspension": "MacPherson strut"
        },
        "image_url": "https://www.mazdausa.com/siteassets/vehicles/2024/mazda3-sedan/build-and-price/trims/34-jellies/preferred/fwd/2024-mazda-3-sedan-2.5-s-preferred-package"
    }
]