import streamlit as st
import requests

st.title("Nyaya AI Reasoning System")

text = st.text_input("Enter argument:")

if st.button("Analyze"):
    res = requests.post("http://127.0.0.1:8000/analyze", params={"text": text})
    data = res.json()

    st.subheader("Argument")
    st.write(data["argument"])

    st.subheader("Nyaya Mapping")
    st.write(data["nyaya"])

    st.subheader("Inference")
    st.write(data["inference"])

    st.subheader("Fallacy")
    st.write(data["fallacy"])