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
    image = Image.open('images/appendectomy/appendectomy.png')
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
      st.write("Laparoscopic cholecystectomy or the removal of the gallbladder, is a common surgical procedure to treat gallstones and the problems they cause, such as abdominal pain or infection. The gallbladder is an organ that sits under the liver and stores bile. Bile is released into the intestinal tract during meals to help break down fat. The surgery is performed under general anesthesia. Small incisions are made on the abdomen to allow for a camera and surgical tools to be placed inside the abdomen. The gallbladder is then removed carefully from the liver and out of the abdomen. The abdomen is closed with sutures and dressings are placed on the abdomen to keep the area clean. After surgery, patients are brought to the recovery room to wake up from anesthesia and address any postoperative needs such as pain and nausea. Typically, patients are discharged the same day of surgery. ")
      st.header("Preoperative Instructions")
      st.write("Preparing for surgery is important to help improve recovery and outcomes. You will receive a phone call or an in-person visit at a preoperative clinic to manage any chronic conditions and prepare patients for an upcoming surgery. You may receive instructions to draw labs, receive tests, or see a specialist for consultation before surgery to ensure the patient is optimized for surgery and decrease the risk of surgery and anesthesia. To prepare for surgery weeks before surgery, it is important to stay active and eat well. Please practice deep breathing exercises to prevent any lung complications during and after surgery. During the preoperative clinic visit, a clinician will explain to you what medications to take or hold before surgery. It is important to stop any dietary supplements for at least one week before surgery. ")
      st.header("Day of Surgery Instructions")
      st.write("It is important to alert your surgeon if you are not feeling well or experiencing any upper respiratory symptoms before surgery, as this may increase the risk of surgery and anesthesia. Please stop eating 8 hours and drinking clear fluids 2 hours before arriving for surgery. Please hold any medications the morning of surgery as directed by your preoperative clinic visit. You will arrive at the admitting office at the hospital and they will direct you to our preoperative surgical area. At the preoperative area you will be checked in by the preoperative nurse and receive an intravenous catheter for medications to be administered. You will meet different members of the surgical team including an operating room nurse, an anesthesia care provider (either an anesthesiologist or nurse anesthetist), as well as the surgeon. You will then be transferred to the operating room where the surgery will take place.")
      st.header("Postoperative Instructions")
      st.write("After surgery, you will recover in the recovery room, also known as the post anesthesia recovery unit (PACU). You may experience abdominal discomfort or pain, nausea, drowsiness, and shoulder pain. The recovery room team consisting of nurses and anesthesiologists will help manage these issues. Typically, you will have sutures that close the wounds made during surgery. Depending on the type of suture, removal of the sutures will be necessary during a follow-up visit. There will be a large dressing over the wound site, and a small adhesive dressing on the wound under the large dressing. You may remove the large dressing in 48 hours after surgery, or if the dressing is soiled. Keep the small adhesive dressings on for 7 days after surgery. You can take a shower 48 hours after the surgery, please do not soak the wounds in water. Prior to 48 hours, you can take a sponge bath and be sure to not get the wound sites wet. You will be prescribed non-opioid pain medications that can be taken around the clock. This includes acetaminophen and ibuprofen. You will also receive anti-nausea medication to help during recovery. Typically, pain will be mild to moderate for the first 48 hours, and slowly improve in a week after surgery. Please refrain from heavy lifting for at least 2 weeks. ")
  else:
     st.write("Sorry, there are no current extra resources for this surgery. Please continue to ask Patient Co-Pilot if you have any questions!")


