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
    st.title("Details About the Dataset Used")
    st.write("this dataset collects various physical, structural, and environmental features of mushrooms, likely for the purpose of classification or identification. The attributes cover aspects of morphology (cap, stem, gills), reproduction (spores), and ecological context (habitat, season).")
    st.markdown("""
- id: A unique identifier for each mushroom sample.
- class: The classification of the mushroom, potentially indicating whether it is edible or poisonous.
- cap-diameter: The diameter of the mushroom cap, which is the top part of the mushroom, likely measured in centimeters or millimeters.
- cap-shape: The shape of the mushroom's cap (e.g., bell-shaped, convex, flat, etc.).
- cap-surface: The texture or surface type of the mushroom's cap (e.g., smooth, scaly, or rough).
- cap-color: The color of the mushroom's cap (e.g., white, brown, red, etc.).
- does-bruise-or-bleed: Indicates whether the mushroom bruises or exudes liquid when damaged (could be a yes/no or binary value).
- gill-attachment: How the gills (the spore-producing structures under the cap) are attached to the stem (e.g., free, attached, or descending).
- gill-spacing: The spacing of the gills, which could be closely spaced or widely spaced.
- gill-color: The color of the gills, which can vary and is important for identification (e.g., white, pink, brown).
- stem-height: The height of the mushroom stem, possibly in centimeters or millimeters.
- stem-width: The thickness or diameter of the mushroom stem.
- stem-root: The type of root structure of the stem (e.g., bulbous, rooted, etc.).
- stem-surface: The surface texture of the stem (e.g., smooth, fibrous, or scaly).
- stem-color: The color of the mushroom stem (e.g., white, brown, yellow).
- veil-type: The type of veil covering the mushroom's gills or stem before it opens (e.g., partial or universal veil).
- veil-color: The color of the veil, which can help in identification.
- has-ring: Indicates if the mushroom has a ring around the stem (yes/no).
- ring-type: The type of ring around the stem (e.g., large, small, or double).
- spore-print-color: The color of the spores when a mushroom cap is placed on paper, which can be a key identifier (e.g., white, black, brown).
- habitat: The environment where the mushroom is typically found (e.g., woods, fields, meadows).
- season: The time of year when the mushroom is commonly found (e.g., spring, summer, autumn).
""")

elif option == "About":
    st.title("About")
    st.write("This app is created to demonstrate navigation using Streamlit.")

elif option == "Contact":
    st.title("Contact Us")
    st.write("Feel free to reach out via our contact form or social media.")
elif option=="Approach/Links":
    st.title('Approach')
    st.title("Links")