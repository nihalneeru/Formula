import streamlit as st

# Custom CSS to include the Google Font and style the header
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

</style>
"""

# Place the CSS at the top of the app
st.markdown(header_css, unsafe_allow_html=True)

# Using a single column for the header to ensure the background covers the entire row
st.markdown("<div class='header-container'><div class='header'>ApexAI</div></div>", unsafe_allow_html=True)

# Your main content starts here
st.title("ApexAI")

# Example content
st.write("Explore the thrilling world of racing. Dive into live simulations and much more.")

# Insert containers separated into tabs:
tab1, tab2 = st.tabs(["Home", "Race Mode"])
tab1.write("Home")
tab2.write("Race Mode")

# You can also use "with" notation:
with tab1:
    st.radio('Select one:', [1, 2])
