import streamlit as st
import pandas as pd
import pydeck as pdk
from cars import cars
from streamlit_drawable_canvas import st_canvas
from PIL import Image
import io
from pymongo import MongoClient
from bson.objectid import ObjectId

MONGO_URI = "mongodb+srv://nihal41:Nihal2004!@cluster0.jumqmmz.mongodb.net/"
DATABASE_NAME = "formula"
client = MongoClient(MONGO_URI)
db = client[DATABASE_NAME]

# CSS for styling
header_css = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Ubuntu:wght@400;700&display=swap');

/* Header styling */
.header {
    background-color: red;
    color: white;
    padding: 10px 0px;
    font-size: 28px; /* Slightly larger font for the header */
    font-family: 'Ubuntu', sans-serif; /* No cursive for clean look */
    text-align: center; /* Centered header text */
}

/* File uploader styling */
.fileUploader {
    border: 2px solid #e6e6e6;
    border-radius: 5px;
    padding: 15px;
    margin: 25px 0; /* More space around uploader */
}

.fileUploader label {
    display: block; /* Makes the label take the full width */
    color: black;
    background-color: red;
    padding: 10px;
    margin: 0; /* Reset margin for the label */
    border-radius: 5px;
    text-align: center; /* Centered text in button */
    font-family: 'Ubuntu', sans-serif;
}

/* Style the button to match your theme */
.fileUploader .stButton > button {
    width: 100%; /* Full-width button */
    border-radius: 5px;
    font-family: 'Ubuntu', sans-serif;
    font-weight: 700; /* Bold font weight for button text */
}

/* Tabs */
.stTabs {
    margin: 20px 0; /* Space around tabs */
}

/* Individual tab styling */
.stTab {
    font-family: 'Ubuntu', sans-serif;
    font-size: 18px; /* Larger font size for tabs */
}

/* Override Streamlit's default styling */
.css-1d391kg {
    padding: 0;
}
</style>
"""

st.markdown(header_css, unsafe_allow_html=True)
st.markdown("<div class='header'>ApexAI</div>", unsafe_allow_html=True)
st.markdown("<div class='content'>", unsafe_allow_html=True)
st.title("Explore the thrilling world of racing")
st.write("Dive into live simulations and much more.")
st.markdown("</div>", unsafe_allow_html=True)

tab1, tab2, tab3, tab4, tab5 = st.tabs(["Home", "Choose a Car", "Select a Track", "Make a Track", "Test Drive!"])

with tab1:
    st.markdown("## Welcome to ApexAI Racing Simulator")
    st.markdown("""
        Follow these steps to get started:
        
        1. **Choose a Car**: Select your favorite racing car to begin.
        2. **Track Selection**:
            - **Make Your Own Track**: Unleash your creativity by designing your very own track.
            - **Select a Professional Formula One Track**: Choose from a list of iconic Formula One tracks.
        3. **Test Drive**: Put your car and track to the test in a virtual race.
    """)
    
    if st.button('Choose a Car'):
        st.experimental_set_query_params(page='Choose a Car')
        st.experimental_rerun()
    
    if st.button('Make Your Own Track'):
        # Implement track creation functionality here
        st.write("Track creation page")
        
    if st.button('Select a Professional Formula One Track'):
        # Implement track selection functionality here
        st.write("Track selection page")
        
    if st.button('Test Drive'):
        # Implement test drive functionality here
        st.write("Test drive page")

with tab2:
    DATABASE_NAME = "formula"  # The name of the database
    COLLECTION_NAME = "cars"  # The name of the collection

    client = MongoClient(MONGO_URI)
    db = client[DATABASE_NAME]
    collection = db[COLLECTION_NAME]

    def send_to_mongodb(car_data):
        try:
            # The filter {} will match any document, and upsert=True will insert if it doesn't exist
            result = collection.replace_one({}, car_data, upsert=True)
            if result.acknowledged:
                st.success(f"Car data updated in MongoDB. Modified count: {result.modified_count}")
            else:
                st.error("Failed to update car data in MongoDB.")
        except Exception as e:
            st.error(f"An error occurred while sending data to MongoDB: {e}")

    def select_and_send_car_info(cars):
        """Displays car selection UI and sends the selected car's data to MongoDB."""
        car_names = [car["name"] for car in cars]
        selected_car_name = st.selectbox("Select a car", car_names)
        selected_car = next((car for car in cars if car["name"] == selected_car_name), None)

        if selected_car:
            # Display car specifications and image
            col1, col2 = st.columns([2, 3])
            with col1:
                st.subheader(selected_car["name"])
                st.write(f"**Type:** {selected_car['type']}")
                st.write("**Specifications:**")
                for spec_key, spec_value in selected_car["specifications"].items():
                    st.write(f"**{spec_key.replace('_', ' ').capitalize()}:** {spec_value}")

            with col2:
                if 'image_url' in selected_car:
                    st.image(selected_car["image_url"], use_column_width=True, caption=selected_car["name"])
            
            # If the button is clicked, send car data to MongoDB
            if st.button(f"Select {selected_car['name']}"):
                send_to_mongodb(selected_car)

    st.header("Choose Your Car")
        # Call the function to display car options and handle the selection
    select_and_send_car_info(cars)
with tab3:
    TRACK_COLLECTION_NAME = "tracks"  # The name of the tracks collection
    track_collection = db[TRACK_COLLECTION_NAME]

    def send_track_to_mongodb(track_data):
        try:
            # Using replace_one with upsert=True to ensure only one document exists
            result = track_collection.replace_one({}, track_data, upsert=True)
            if result:
                st.success(f"Track data upserted to MongoDB successfully with ID: {result.upserted_id if result.upserted_id else 'existing document updated.'}")
            else:
                st.error("Failed to upsert track data to MongoDB.")
        except Exception as e:
            st.error(f"An error occurred while sending data to MongoDB: {e}")
    
    track_info = [
    {"name": "Silverstone Circuit", "location": "United Kingdom", "image": "tracks/silverstone.png", "lat": 52.0733, "lon": -1.0147},
    {"name": "Monza Circuit", "location": "Italy", "image": "tracks/monza.png", "lat": 45.6156, "lon": 9.2811},
    {"name": "Circuit de Spa-Francorchamps", "location": "Belgium", "image": "tracks/spa.png", "lat": 50.4357, "lon": 5.9695},
    {"name": "Interlagos", "location": "Brazil", "image": "tracks/interlagos.png", "lat": -23.7022, "lon": -46.6932},
    {"name": "Marina Bay Street Circuit", "location": "Singapore", "image": "tracks/marina.png", "lat": 1.2882, "lon": 103.8585},
    {"name": "Yas Marina Circuit", "location": "Abu Dhabi", "image": "tracks/yas.png", "lat": 24.46993, "lon": 54.60546},
    {"name": "Hockenheimring", "location": "Germany", "image": "tracks/hocken.png", "lat": 49.32716, "lon": 8.56560},
    {"name": "Bahrain International Circuit", "location": "Bahrain", "image": "tracks/bahrain.png", "lat": 26.03218, "lon": 50.51090},
    {"name": "Circuit of the Americas", "location": "USA", "image": "tracks/cota.png", "lat": 30.133883, "lon": -97.641144},
    ]

    df_tracks = pd.DataFrame(track_info)

    if 'selected_track' not in st.session_state:
        st.session_state.selected_track = None

    # Display the selected track at the top
    if st.session_state.selected_track:
        st.success(f"You have selected: {st.session_state.selected_track}")

    # Button to control the map visibility
    if st.button('View Map'):
        st.session_state.map_expanded = True

    # Conditionally render the map expander if map_expanded is True in the session state
    if st.session_state.get('map_expanded', False):
        with st.expander("Map", expanded=True):
            map_layer = pdk.Layer(
                'ScatterplotLayer',
                data=df_tracks,
                get_position='[lon, lat]',
                get_color='[200, 30, 0, 160]',
                get_radius=50000,
            )
            st.pydeck_chart(pdk.Deck(
                map_style='mapbox://styles/mapbox/light-v9',
                initial_view_state=pdk.ViewState(latitude=df_tracks['lat'].mean(), longitude=df_tracks['lon'].mean(), zoom=1, pitch=0),
                layers=[map_layer],
                tooltip={"html": "<b>{name}</b><br><b>{location}</b>", "style": {"backgroundColor": "steelblue", "color": "white"}}
            ))

    # Tracks Display
    tracks_per_row = 3
    for i in range(0, len(track_info), tracks_per_row):
        cols = st.columns(tracks_per_row)
        for j, track in enumerate(track_info[i:i+tracks_per_row]):
            with cols[j]: 
                st.image(track["image"], use_column_width=True, caption=f"{track['name']} - {track['location']}")
                if st.button('Select', key=f'select{track["name"]}'):
                    track_data = {
                        "name": track['name'],
                        "image": track['image']  # Assuming 'image' is a URL or a binary data
                    }
                    send_track_to_mongodb(track_data)
with tab4:
    st.subheader("Make Your Own Racetrack")
    uploaded_file = st.file_uploader("Upload your racetrack image", type=["jpg", "jpeg", "png"], key="file_uploader")

    background_image = None
    if uploaded_file is not None:
        # Open the uploaded image with PIL
        background_image = Image.open(uploaded_file)
        st.success("Image uploaded successfully!")
        st.image(uploaded_file, caption='Uploaded Racetrack.', use_column_width=True)

    st.title("Draw and Save Image")

    # Setup canvas with a nicer border and larger size
    st.markdown("""
    <style>
    .canvas-container {
        border: 2px dashed #000;
        border-radius: 5px;
    }
    </style>
    """, unsafe_allow_html=True)

    # Create a canvas component
    canvas_result = st_canvas(
        fill_color="rgba(255, 165, 0, 0.3)",  # Filler color
        stroke_width=5,
        stroke_color="#000000",  # Black pen color
        background_color="#FFFFFF",
        background_image=background_image,
        update_streamlit=True,
        height=600,  # Increased height
        width=800,  # Increased width
        drawing_mode="freedraw",
        key="canvas",
    )

    # If there is canvas data
    if canvas_result.image_data is not None:
        # Convert the canvas data to a PIL Image
        im = Image.fromarray(canvas_result.image_data.astype('uint8'), mode="RGBA")
        # Convert to bytes
        buf = io.BytesIO()
        im.save(buf, format='PNG')
        byte_im = buf.getvalue()

        # Create a download button for the image
        st.download_button(
            label="Download Image",
            data=byte_im,
            file_name="drawing.png",
            mime="image/png"
        )
    with tab5:
        st.subheader("Race Mode")
        st.radio('Select one:', ["Weather", "Track"], index=0)
