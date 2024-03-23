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
