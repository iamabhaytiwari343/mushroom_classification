import streamlit as st

# Set up sidebar layout with buttons styled like rectangular boxes
st.sidebar.title("Mushroom Classifier")

# Define a function for button style
def button_style():
    st.markdown("""
        <style>
        .block-container { padding-top: 2rem; }
        .stButton > button {
            border-radius: 5px;
            margin-bottom: 10px;
            width: 100%;
            padding: 10px;
            font-size: 16px;
            background-color: #f5f5f5;
            border: 1px solid #ddd;
        }
        .stButton > button:hover {
            background-color: #ececec;
        }
        </style>
    """, unsafe_allow_html=True)

# Apply the button style
button_style()

# Sidebar buttons for navigation
description=st.sidebar.markdown("### Welcome to Our App")
dd2=st.sidebar.markdown("""
- The goal of this Project is to predict whether a mushroom is edible or poisonous based on its physical characteristics. 
- You can visit the original dataset https://archive.ics.uci.edu/dataset/73/mushroom .
""")
# Display corresponding content based on the button clicked")
home_btn = st.sidebar.button("About the Dataset")
about_btn = st.sidebar.button("Data Visualization")
contact_btn = st.sidebar.button("Prediction")
setdapp=st.sidebar.button("Approach/Links")


# Determine which button was clicked
if home_btn:
    option = "About the Dataset"
elif about_btn:
    option = "About"
elif contact_btn:
    option = "Contact"
elif setdapp:
    option = "Approach/Links"
else:
    option = "About the Dataset"  # Default to Home if no button is clicked yet


if option == "About the Dataset":
    st.title("Welcome to the Home Page")
    st.write("This is the home page of the app.")

elif option == "About":
    st.title("About")
    st.write("This app is created to demonstrate navigation using Streamlit.")

elif option == "Contact":
    st.title("Contact Us")
    st.write("Feel free to reach out via our contact form or social media.")
elif option=="Approach/Links":
    st.title('Approach')
    st.title("Links")