import streamlit as st

st.title('Resources 📚')

if "surgery" not in st.session_state:
  st.write("Please inform the Patient Co-Pilot of your surgery through the home page chatbot to obtain resources.")