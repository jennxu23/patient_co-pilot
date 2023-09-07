# Patient Co-Pilot
Patient Co-Pilot is a tool intended to help guide patients through their surgery. It uses the ChatGPT API, combined with a specific prompt, to leverage LLMs to answer patient questions about their surgeries. It also includes static informational text and images tailored to the patients' surgery. Patient Co-Pilot is intended to be a helpful tool to streamline communication between patients and doctors. 

Winner of the August 2023 Health Universe Hackathon

## Setting up the environment
To set up the environment, first create the environment: `conda create --name op_assistant`.
Then, activate the environment with `conda activate op_assistant`.
Then, to install the necessary packages, run `pip install requirements.txt`.
This app requires an OpenAI API key to run. To connect the app to your OpenAI Key, run `export OPENAI_KEY = <your_key>` in your terminal.

## Running the app
Once you get the environment set up, run `streamlit run home_page.py ` to run the app. The app will prompt you to enter a surgery. The resources page will populate with information about your surgery, and then you can use the chatbot to learn more about your surgery. Currenlty, we have resources loaded in for an appendectomy and a Laparoscopic cholecystectomy.

## Collaborators
Mishaal Ali MD, Kate Callon, Jennifer Xu, Edward Yap MD
