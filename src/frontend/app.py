import streamlit as st
import requests

st.title("Nyaya AI Reasoning System")

text = st.text_input("Enter argument:")

if st.button("Analyze"):
    res = requests.post("http://127.0.0.1:8000/analyze", params={"text": text})
    data = res.json()

    st.subheader("🧠 Nyaya Reasoning")

    st.write("Paksha:", data["nyaya"]["paksha"])
    st.write("Hetu:", data["nyaya"]["hetu"])
    st.write("Vyapti:", data["nyaya"]["vyapti"])

    st.subheader("⚖️ Inference")
    st.write(data["inference"])

    st.subheader("📖 Explanation")
    st.write(data["explanation"])