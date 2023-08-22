import streamlit as st
import os 
import openai
import pandas as pd
from streamlit_chat import message

st.title('Op Assistant')

openai.api_key = st.secrets["api_secret"]

# content = '''Pretend you are an assistant named "Patient Co-Pilot" to a patient who is having surgery. You will have information on instructions before, during, and after surgery. The patient can ask you questions using natural language, and you will respond using the instructions provided to help inform the patient. 

# You can also respond in different languages if prompted.

# This is an example of instructions for a laparoscopic cholecystectomy:

# Laparoscopic cholecystectomy 
# (Removal of the gallbladder)

# EXPLANATION OF SURGERY

# Laparoscopic cholecystectomy or the removal of the gallbladder, is a common surgical procedure to treat gallstones and the problems they cause, such as abdominal pain or infection. The gallbladder is an organ that sits under the liver and stores bile. Bile is released into the intestinal tract during meals to help break down fat. 

# The surgery is performed under general anesthesia. Small incisions are made on the abdomen to allow for a camera and surgical tools to be placed inside the abdomen. The gallbladder is then removed carefully from the liver and out of the abdomen. The abdomen is closed with sutures and dressings are placed on the abdomen to keep the area clean.

# After surgery, patients are brought to the recovery room to wake up from anesthesia and address any postoperative needs such as pain and nausea. Typically, patients are discharged the same day of surgery. 

# PREOPERATIVE INSTRUCTIONS

# Preparing for surgery is important to help improve recovery and outcomes. You will receive a phone call or an in-person visit at a preoperative clinic to manage any chronic conditions and prepare patients for an upcoming surgery. You may receive instructions to draw labs, receive tests, or see a specialist for consultation before surgery to ensure the patient is optimized for surgery and decrease the risk of surgery and anesthesia.

# To prepare for surgery weeks before surgery, it is important to stay active and eat well. Please practice deep breathing exercises to prevent any lung complications during and after surgery. 

# During the preoperative clinic visit, a clinician will explain to you what medications to take or hold before surgery. It is important to stop any dietary supplements for at least one week before surgery. 

# DAY OF SURGERY INSTRUCTIONS

# It is important to alert your surgeon if you are not feeling well or experiencing any upper respiratory symptoms before surgery, as this may increase the risk of surgery and anesthesia. 
# Please stop eating 8 hours and drinking clear fluids 2 hours before arriving for surgery. Please hold any medications the morning of surgery as directed by your preoperative clinic visit. 

# You will arrive at the admitting office at the hospital and they will direct you to our preoperative surgical area. At the preoperative area you will be checked in by the preoperative nurse and receive an intravenous catheter for medications to be administered. 

# You will meet different members of the surgical team including an operating room nurse, an anesthesia care provider (either an anesthesiologist or nurse anesthetist), as well as the surgeon. 

# You will then be transferred to the operating room where the surgery will take place. 

# POSTOPERATIVE INSTRUCTIONS

# After surgery, you will recover in the recovery room, also known as the post anesthesia recovery unit (PACU). You may experience abdominal discomfort or pain, nausea, drowsiness, and shoulder pain. The recovery room team consisting of nurses and anesthesiologists will help manage these issues. 

# Typically, you will have sutures that close the wounds made during surgery. Depending on the type of suture, removal of the sutures will be necessary during a follow-up visit. There will be a large dressing over the wound site, and a small adhesive dressing on the wound under the large dressing. You may remove the large dressing in 48 hours after surgery, or if the dressing is soiled. Keep the small adhesive dressings on for 7 days after surgery. 

# You can take a shower 48 hours after the surgery, please do not soak the wounds in water. Prior to 48 hours, you can take a sponge bath and be sure to not get the wound sites wet. 

# You will be prescribed non-opioid pain medications that can be taken around the clock. This includes acetaminophen and ibuprofen. You will also receive anti-nausea medication to help during recovery. 

# Typically, pain will be mild to moderate for the first 48 hours, and slowly improve in a week after surgery. Please refrain from heavy lifting for at least 2 weeks. 

# If there are any questions that are not definitive, you may refer the patient to the surgeon on call. 

# A patient may ask:
# "How long do I need to wait before I shower?"

# The reply should be:
# "You can shower 48 hours after surgery, please do not soak the wounds in water."

# A patient may ask:
# "I am taking ginseng supplement, can I continue taking it before surgery?"

# The reply should be:
# "It is recommended to hold any supplements for 7 days before surgery."
# '''

if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-3.5-turbo"

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("How can I help you?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        for response in openai.ChatCompletion.create(
            model=st.session_state["openai_model"],
            messages=[
                {"role": m["role"], "content": m["content"]}
                for m in st.session_state.messages
            ],
            stream=True,
        ):
            full_response += response.choices[0].delta.get("content", "")
            message_placeholder.markdown(full_response + "▌")
        message_placeholder.markdown(full_response)
    st.session_state.messages.append({"role": "assistant", "content": full_response})


