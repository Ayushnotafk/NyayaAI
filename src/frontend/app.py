import streamlit as st
import requests

# Page config
st.set_page_config(page_title="INFER AI", page_icon="🧠", layout="centered")

st.title("🧠 INFER AI")

# Input
text = st.text_input("Enter argument:")

# Button
if st.button("Analyze"):

    if text.strip() == "":
        st.warning("Please enter an argument.")
        st.stop()

    try:
        with st.spinner("Analyzing using Nyaya reasoning... ⏳"):
            res = requests.post(
                "http://127.0.0.1:8000/analyze",
                json={"text": text}
            )

        # API error handling
        if res.status_code != 200:
            st.error(f"API Error: {res.status_code}")
            st.text(res.text)
            st.stop()

        data = res.json()

    except Exception as e:
        st.error("Backend not responding or invalid JSON")
        st.text(str(e))
        st.stop()

    # Backend error handling
    if "error" in data:
        st.error(data["error"])
        st.stop()

    # ---------- OUTPUT ----------

    # Nyaya Reasoning
    st.subheader("📜 Nyaya Reasoning")

    st.info(f"""
**Paksha (Conclusion):** {data["nyaya"]["paksha"]}

**Hetu (Reason):** {data["nyaya"]["hetu"]}

**Vyapti (Rule):** {data["nyaya"]["vyapti"]}
""")

    # Inference
    st.subheader("🔍 Inference")
    st.success(data["inference"])

    # Explanation
    st.subheader("💡 Explanation")

    explanation = data["explanation"]

    # Format nicely
    explanation = explanation.replace("Paksha (Conclusion):", "\n**Paksha (Conclusion):**")
    explanation = explanation.replace("Hetu (Reason):", "\n**Hetu (Reason):**")
    explanation = explanation.replace("Vyapti (Rule):", "\n**Vyapti (Rule):**")
    explanation = explanation.replace("Final Result:", "\n\n### Final Result\n")

    st.markdown(explanation)