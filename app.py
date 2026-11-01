import streamlit as st

st.title("Smart age calculator program")

birth_year = st.number_input("Enter your birth year:", min_value=1900, max_value=2026, value=2000)

if st.button("calculate my age"):
    age = 2026 - birth_year
    st.success(f"your age is: {age}")
