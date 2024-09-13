import streamlit as st
import pickle
# Set up sidebar layout with buttons styled like rectangular boxes
with open("lgb_model.pkl", "rb") as file:
    model = pickle.load(file)

# Function to make predictions using the model
def predict(features):
    return model.predict([features])
# Ensure the session state for selected page is initialized
if 'page' not in st.session_state:
    st.session_state['page'] = 'Home'  # Default to 'Home' on initial load


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
    st.session_state['page'] = "About the Dataset"
elif about_btn:
    st.session_state['page'] = "Data Visualization"
elif contact_btn:
    st.session_state['page'] = "Prediction"
elif setdapp:
    st.session_state['page'] = "Approach/Links"


if st.session_state['page'] == "About the Dataset":
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

elif st.session_state['page'] == "Data Visualization":
    st.title("Data Visualization")
    st.write("This app is created to demonstrate navigation using Streamlit.")




elif st.session_state['page'] == "Prediction":
    st.title("Predict/Classify")
    # Create a form for input features (adjust fields as per your model)
    st.subheader("Enter input values for prediction:")
    
    # Numerical inputs
    feature_1 = st.number_input("cap-diameter", value=0.0, min_value=0.0, max_value=82.0)
    feature_9 = st.number_input("stem-height", value=0.0)
    feature_10 = st.number_input("stem-width", value=0.0)

    # Categorical inputs (adjust options as needed)
    feature_2 = st.selectbox("cap-shape", options=['f', 'x', 'p', 'b', 'o', 'c', 's', 'noise'])
    feature_3 = st.selectbox("cap-surface", options=['s', 'h', 'y', 'l', 't', 'e', 'g', 'missing', 'd', 'i', 'w', 'k', 'noise'])
    feature_4 = st.selectbox("cap-color", options=['u', 'o', 'b', 'g', 'w', 'n', 'e', 'y', 'r', 'p', 'k', 'l', 'noise'])
    feature_5 = st.selectbox("does-bruise-or-bleed", options=['f', 't', 'noise'])
    feature_6 = st.selectbox("gill-attachment", options=['a', 'x', 's', 'd', 'e', 'missing', 'f', 'p', 'noise'])
    feature_7 = st.selectbox("gill-spacing", options=['c', 'missing', 'd', 'f', 'noise'])
    feature_8 = st.selectbox("gill-color", options=['w', 'n', 'g', 'k', 'y', 'f', 'p', 'o', 'b', 'u', 'e', 'r', 'noise'])
    feature_11 = st.selectbox("stem-root", options=['missing', 'b', 'c', 'r', 's', 'f', 'noise'])
    feature_12 = st.selectbox("stem-surface", options=['missing', 'y', 's', 't', 'g', 'h', 'k', 'i', 'f', 'noise'])
    feature_13 = st.selectbox("stem-color", options=['w', 'o', 'n', 'y', 'e', 'u', 'p', 'f', 'g', 'r', 'k', 'l', 'b', 'noise'])
    feature_14 = st.selectbox("veil type", options=['missing', 'u', 'noise'])
    feature_15 = st.selectbox("veil-color", options=['missing', 'n', 'w', 'k', 'y', 'e', 'u', 'noise'])
    feature_16 = st.selectbox("has-ring", options=['f', 't', 'noise'])
    feature_17 = st.selectbox("ring-type", options=['f', 'z', 'e', 'missing', 'p', 'l', 'g', 'r', 'm', 'noise'])
    feature_18 = st.selectbox("spore-print-color", options=["missing", "noise","k","p","w","n","r","u","g"])
    feature_19 = st.selectbox("habitat", options=["d", "g","l","m","h","w","p","u","noise"])
    feature_20 = st.selectbox("season", options=["a", "u", "w","s"])


    if st.button("Predict"):
        # Collect all input features into a list
        features = [
            feature_1, feature_2, feature_3, feature_4, feature_5, feature_6, feature_7,
            feature_8, feature_9, feature_10, feature_11, feature_12, feature_13, feature_14,
            feature_15, feature_16, feature_17, feature_18, feature_19, feature_20
        ]

        # Make prediction using the loaded model
        prediction = predict(features)

        # Display the prediction result
        st.success(f"The prediction is: {prediction[0]}")




elif st.session_state['page']=="Approach/Links":
    st.title('Approach')
    st.title("Links")