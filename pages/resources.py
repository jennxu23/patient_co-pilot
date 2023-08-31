import streamlit as st
from PIL import Image

st.title('Resources 📚')

if "surgery" not in st.session_state:
  st.write("Please inform the Patient Co-Pilot of your surgery through the home page chatbot to obtain resources.")

else:

  if "appendectomy" in st.session_state["surgery"]:
    st.header("What is Appendicitis?")
    st.write("Appendicitis is an infection of the appendix, which is a small pouch-like organ located in the lower right side of the abdomen. The infection and swelling of the appendix can lead to a decrease in blood supply, causing tissue death and potentially leading to a ruptured appendix. A ruptured appendix can release bacteria and stool into the abdomen, resulting in a condition called peritonitis, which is an infection of the entire abdomen. Appendicitis is most commonly seen in individuals between the ages of 10 and 30 years old and is a common reason for surgery in children. It is also the most common surgical emergency in pregnancy. Appendectomy, the surgical removal of the appendix, is the standard treatment for appendicitis.")
    st.header("How is it treated? ")
    st.write("Appendicitis is typically treated with appendectomy, which is the surgical removal of the appendix. This is the standard treatment for appendicitis and is performed to prevent complications such as a ruptured appendix and inflammation and infection in the abdomen.")
    st.write("In some cases, antibiotic treatment may be used to treat appendicitis if there is no rupture. This approach may result in fewer complications, less sick leave, and less pain medication compared to surgery. However, there is a higher chance of appendicitis returning with antibiotic treatment alone.")
    st.write("Laparoscopic appendectomy: The appendix is removed using tools through small incisions in the lower right abdomen.")
    st.write("Open appendectomy: the appendix is removed through an incision in the abdomen.")
    st.write("It is important to note that if appendicitis is left untreated and the appendix ruptures, it can lead to more serious complications. A ruptured appendix may occur in up to 32 percent of patients with acute appendicitis.")
    image = Image.open('images/appendectomy/appendectomy2.png')
    st.image(image, caption='Visual of Laparoscopic vs Open Appendectomy')
    st.header("What is a laparoscopic appendectomy? ")
    st.write("Laparoscopic appendectomy is a minimally invasive surgical technique used to remove the appendix.")
    st.write("The procedure involves making 1 to 3 small incisions in the abdomen, through which a laparoscope (a telescope-like instrument with a light and camera) and surgical instruments are inserted.")
    st.write("Carbon dioxide gas is used to inflate the abdomen, allowing the surgeon to visualize the appendix more easily.")
    st.write("The infected appendix is then removed using surgical instruments, and the area is washed with sterile fluid to reduce the risk of further infection.")
    st.write("The carbon dioxide gas is released through the incisions, which are then closed with sutures, staples, or covered with a glue-like bandage or Steri-Strips.")
    st.write("In some cases, the surgeon may need to switch to an open technique during the procedure, especially in males, individuals over 40 years old, diabetics, obese individuals, or those with a ruptured appendix.")
    st.header("What are the potential risks of the procedure?")
    st.write("Risks associated with laparoscopic appendectomy may include infection at the incision sites or within the abdomen, which can lead to complications such as abscess formation or peritonitis (inflammation in the abdomen).")
    st.write("There is a small risk of bleeding during the procedure, which may require additional intervention.")
    st.write("In rare cases, injury to surrounding organs such as the intestines, blood vessels, or bladder may occur during the surgery.")
    st.write("Some patients may experience pain or discomfort at the incision sites after the procedure.")
    st.write("There is a possibility of conversion to an open procedure if the surgeon encounters difficulties or complications during the laparoscopic approach.")
    st.write("As with any surgical procedure, there is a risk of adverse reactions to anesthesia.")
  elif "Laparoscopic cholecystectomy" in st.session_state["surgery"]:
      st.header("What is Laparoscopic cholecystectomy?")
  else:
     st.write("Sorry, there are no current extra resources for this surgery. Please continue to ask Patient Co-Pilot if you have any questions!")


