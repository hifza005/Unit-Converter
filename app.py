import os
import streamlit as st

def load_css():
    css_file = "styles.css"
    if os.path.exists(css_file):
        with open(css_file, "r") as f:
            css = f.read()
            st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)

load_css()  # Load the styles


# Unit conversion dictionaries
distance_units = {
    "Meters": 1,
    "Kilometers": 1000,
    "Feet": 0.3048,
    "Miles": 1609.34,
    "Yards": 0.9144,
    "Inches": 0.0254,
    "Centimeters": 0.01,
    "Millimeters": 0.001,
}

weight_units = {
    "Kilograms": 1,
    "Grams": 0.001,
    "Milligrams": 0.000001,
    "Pounds": 0.453592,
    "Ounces": 0.0283495,
    "Stones": 6.35029,
    "Tons": 1000,  # Metric Ton
}

pressure_units = {
    "Pascals": 1,
    "Hectopascals": 100,
    "Kilopascals": 1000,
    "Bar": 100000,
    "Atmospheres": 101325,
    "Torr": 133.322,
    "mmHg": 133.322,
}

time_units = {
    "Second": 1,
    "Minute": 60,
    "Hours": 3600,
    "Days": 86400,
    "Weeks": 604800,
    "Months": 2592000,
    "Years": 31536000
}

# Converter functions
def distance_converter(from_unit, to_unit, value):
    return value * distance_units[from_unit] / distance_units[to_unit]

def temperature_converter(from_unit, to_unit, value):
    if from_unit == "Celsius":
        if to_unit == "Fahrenheit":
            return (value * 9/5) + 32
        elif to_unit == "Kelvin":
            return value + 273.15
    elif from_unit == "Fahrenheit":
        if to_unit == "Celsius":
            return (value - 32) * 5/9
        elif to_unit == "Kelvin":
            return (value - 32) * 5/9 + 273.15
    elif from_unit == "Kelvin":
        if to_unit == "Celsius":
            return value - 273.15
        elif to_unit == "Fahrenheit":
            return (value - 273.15) * 9/5 + 32
    return value

def weight_converter(from_unit, to_unit, value):
    return value * weight_units[from_unit] / weight_units[to_unit]

def pressure_converter(from_unit, to_unit, value):
    return value * pressure_units[from_unit] / pressure_units[to_unit]

def time_converter(from_unit, to_unit, value):
    return value * time_units[from_unit] / time_units[to_unit]

# Streamlit UI
st.markdown("<h1 class='title-text'>Unit Converter</h1>", unsafe_allow_html=True)


category = st.selectbox("Select Category", ["Distance", "Temperature", "Weight", "Pressure", "Time"])

if category == "Distance":
    from_unit = st.selectbox("From", list(distance_units.keys()))
    to_unit = st.selectbox("To", list(distance_units.keys()))
    value = st.number_input("Enter Value")
    result = distance_converter(from_unit, to_unit, value)
    st.markdown(f'<p class="result-text">{value} {from_unit} is equal to {result:.2f} {to_unit}</p>', unsafe_allow_html=True)

elif category == "Temperature":
    from_unit = st.selectbox("From", ["Celsius", "Fahrenheit", "Kelvin"])
    to_unit = st.selectbox("To", ["Celsius", "Fahrenheit", "Kelvin"])
    value = st.number_input("Enter Value")
    result = temperature_converter(from_unit, to_unit, value)
    st.markdown(f'<p class="result-text">{value} {from_unit} is equal to {result:.2f} {to_unit}</p>', unsafe_allow_html=True)

elif category == "Weight":
    from_unit = st.selectbox("From", list(weight_units.keys()))
    to_unit = st.selectbox("To", list(weight_units.keys()))
    value = st.number_input("Enter Value")
    result = weight_converter(from_unit, to_unit, value)
    st.markdown(f'<p class="result-text">{value} {from_unit} is equal to {result:.2f} {to_unit}</p>', unsafe_allow_html=True)

elif category == "Pressure":
    from_unit = st.selectbox("From", list(pressure_units.keys()))
    to_unit = st.selectbox("To", list(pressure_units.keys()))
    value = st.number_input("Enter Value")
    result = pressure_converter(from_unit, to_unit, value)
    st.markdown(f'<p class="result-text">{value} {from_unit} is equal to {result:.2f} {to_unit}</p>', unsafe_allow_html=True)

elif category == "Time":
    from_unit = st.selectbox("From", list(time_units.keys()))
    to_unit = st.selectbox("To", list(time_units.keys()))
    value = st.number_input("Enter Value")
    result = time_converter(from_unit, to_unit, value)
    st.markdown(f'<p class="result-text">{value} {from_unit} is equal to {result:.2f} {to_unit}</p>', unsafe_allow_html=True)