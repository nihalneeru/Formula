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
        def send_to_pygame_ai(car_data):
            st.success(f"Sending to ApexAI")
        def main():
            st.title("Car Specifications")
            car_names = [car["name"] for car in cars]
            selected_car_name = st.selectbox("Select a car", car_names)
            selected_car = next(car for car in cars if car["name"] == selected_car_name)

            if selected_car:
                col1, col2 = st.columns([2, 3])
                with col1:
                    specifications = selected_car["specifications"]
                    st.subheader(selected_car["name"])
                    st.write(f"**Type:** {selected_car['type']}")
                    st.write("**Specifications:**")
                    spec_table = selected_car["specifications"]
                    for spec_key, spec_value in spec_table.items():
                        st.write(f"**{spec_key.replace('_', ' ').capitalize()}:** {spec_value}")
                with col2:
                    if 'image_url' in selected_car and selected_car["image_url"]:
                        st.image(selected_car["image_url"], use_column_width=True, caption=selected_car["name"])
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

    if 'map_expanded' not in st.session_state:
        st.session_state.map_expanded = False
    if 'selected_track' not in st.session_state:
        st.session_state.selected_track = None

    # Display the selected track at the top
    if st.session_state.selected_track:
        st.success(f"You have selected: {st.session_state.selected_track}")

    # Map Expander
    with st.expander("View Map", expanded=st.session_state.map_expanded):
        # Here we directly set map_expanded to True if the expander is opened
        # It's a direct action, not toggled by the track selection
        st.session_state.map_expanded = True
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

    # Callback function to handle expander state
    def toggle_map_expander():
        st.session_state.map_expanded = not st.session_state.map_expanded

    # Use a separate button or mechanism to explicitly control the map expander state
    # This can be an additional UI element or logic that sets 'map_expanded' independently of track selection

    # Tracks Display
    tracks_per_row = 3
    for i in range(0, len(track_info), tracks_per_row):
        cols = st.columns(tracks_per_row)
        for j, track in enumerate(track_info[i:i+tracks_per_row]):
            with cols[j]: 
                st.image(track["image"], use_column_width=True, caption=f"{track['name']} - {track['location']}")
                if st.button('Select', key=f'select{track["name"]}'):
                    st.session_state.selected_track = track['name']
                    # Do not toggle map_expanded state here
                    st.experimental_rerun()  # Rerun the script
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
