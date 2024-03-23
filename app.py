import streamlit as st
import pandas as pd
import pydeck as pdk
from cars import cars

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

with tab2:
        def send_to_pygame_ai(car_data):
        # Simulate sending data to the Pygame AI model
        # You'll need to replace this with actual code that integrates with your model
            st.success(f"Sending to ApexAI")

        def main():
            st.title("Car Specifications")

        # Create a list of car names for the dropdown menu
            car_names = [car["name"] for car in cars]

        # Let the user select a car name from the dropdown
            selected_car_name = st.selectbox("Select a car", car_names)

        # Find the selected car in the cars list
            selected_car = next(car for car in cars if car["name"] == selected_car_name)

            if selected_car:
                col1, col2 = st.columns([2, 3])  # Adjust the ratio to your preference

                with col1:
                    specifications = selected_car["specifications"]

                    st.subheader(selected_car["name"])
                    st.write(f"**Type:** {selected_car['type']}")
                    st.write("**Specifications:**")
                    spec_table = selected_car["specifications"]
                    for spec_key, spec_value in spec_table.items():
                        st.write(f"**{spec_key.replace('_', ' ').capitalize()}:** {spec_value}")
            
                with col2:
                # Display the car image in a larger size within the second column
                    if 'image_url' in selected_car and selected_car["image_url"]:
                        st.image(selected_car["image_url"], use_column_width=True, caption=selected_car["name"])

            # Button to select the car and send data
                    if st.button("Select Car"):
                        car_data = {
                            "maxSpeed": specifications.get('maxSpeed'),
                            "horsepower": specifications.get('horsepower'),
                            "downforce": specifications.get('downforce')
                        }
                        send_to_pygame_ai(car_data)

        if __name__ == "__main__":
            main()

with tab3:
    
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
    if 'view_map' not in st.session_state:
        st.session_state.view_map = False

    if st.button('View Map'):
        st.session_state.view_map = not st.session_state.view_map

    if st.session_state.view_map:
        st.pydeck_chart(pdk.Deck(
            map_style='mapbox://styles/mapbox/light-v9',
            initial_view_state=pdk.ViewState(
            latitude=df_tracks['lat'].mean(),
            longitude=df_tracks['lon'].mean(),
            zoom=1,
            pitch=0,
        ),
        layers=[
            pdk.Layer(
                'ScatterplotLayer',
                data=df_tracks,
                get_position='[lon, lat]',
                get_color='[200, 30, 0, 160]',
                get_radius=50000,
            ),
        ],
        tooltip={
            "html": "<b>{name}</b><br><b>{location}</b>",
            "style": {
                "backgroundColor": "steelblue",
                "color": "white"
            }
        }
    ))

    tracks_per_row = 3
    
    for i in range(0, len(track_info), tracks_per_row):
        cols = st.columns(tracks_per_row)
        for j in range(tracks_per_row):
            track_index = i + j
            if track_index < len(track_info):
                track = track_info[track_index]
                with cols[j]: 
                    st.image(track["image"], use_column_width=True, caption=f"{track['name']} - {track['location']}")
                    if st.button('Select This Track', key=f'select{track_index}'):
                        st.session_state.selected_track = track['name']
                        st.write(f"You have selected: {track['name']}")
    if 'selected_track' in st.session_state and st.session_state.selected_track:
        st.write(f"Selected track: {st.session_state.selected_track}")

with tab4:
    st.subheader("Make Your Own Racetrack")
    uploaded_file = st.file_uploader("Upload your racetrack image", type=["jpg", "jpeg", "png"], key="file_uploader")
    
    if uploaded_file is not None:
        bytes_data = uploaded_file.getvalue()
        st.success("Image uploaded successfully!")
        st.image(uploaded_file, caption='Uploaded Racetrack.', use_column_width=True)

with tab5:
    st.subheader("Race Mode")
    st.radio('Select one:', ["Weather", "Track"], index=0)
