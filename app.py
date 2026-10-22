
import streamlit as st

st.title("CivicSathi AI")
st.write("Smart Civic Issue Reporting")

issue = st.selectbox(
    "Select a problem",
    ["Pothole", "Garbage", "Streetlight", "Water leakage", "Other"]
)

location = st.text_input("Enter your location")
description = st.text_area("Describe the problem")

if st.button("Submit Report"):
    if location.strip() and description.strip():
        st.success("Your report is ready!")
        st.write("Issue:", issue)
        st.write("Location:", location)
        st.write("Description:", description)
    else:
        st.warning("Please fill in all details.")
      
