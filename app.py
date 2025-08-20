import streamlit as st
from dotenv import load_dotenv
import os
import requests

load_dotenv()
API_KEY = os.getenv("API_KEY")

url = f"https://api.openweathermap.org/data/2.5/weather"
if "cities" not in st.session_state:
    st.session_state.cities = []
st.title("Weather App PRO")
city_input = st.text_input("Find City Weather", "Pyongyang")
if st.button("Add Expander"):
    if city_input: # Only add if the input is not empty
        st.session_state.cities.append(city_input)
        st.success("Expander added!")
    else:
        st.warning("Please enter some content.")

for idx, city in enumerate(st.session_state.cities):
    with st.expander(f"Weather from {city}"):
        params = {
            "q": city,
            "appid": API_KEY,
            "units": "metric"  # temperature in Celsius
        }
        response = requests.get(url, params)
        if response.status_code !=200:
            st.write(F"{city} not found in API")
        data = response.json()
        for key, value in data['main'].items():
            st.write(f"{key}: {value}")
        # st.write(f"Temperature: {data['main']['temp']} degrees Celsius")
        # st.write(f"Humidity: {data['main']['humidity']}%")
        st.write(f"Description: {data['weather'][0]['description']}")
        
# st.session_state.update(st.session_state.cities.append(city_input))
# # for i, city in enumerate(st.session_state.cities):

# # Initialize session state to store expanders
# if "expanders" not in st.session_state:
#     st.session_state.expanders = []

# Text input
# new_text = st.text_input("Enter text to create an expander:")

# # Button to add expander
# if st.button("Add Expander") and new_text:
#     st.session_state.expanders.append(new_text)

# # Display expanders
# for idx, text in enumerate(st.session_state.expanders):
#     with st.expander(f"Expander {idx+1}"):
#         st.write(text)