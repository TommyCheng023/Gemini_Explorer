# Gemini_Explorer
## Description
* A chat interface using `Streamlit` to integrate with Google's cutting-edge large language model, `Gemini`, providing an accessible platform to explore and demonstrate the capabilities of advanced language model applications.
* This project aims to serve as <ins>an educational and practical introduction</ins> to the fusion of large language models and user-friendly interfaces.
## Demo
https://github.com/TommyCheng023/Gemini_Explorer/assets/115842289/154ec337-cbb9-4028-9334-1ca22a3f62e5

## Tutorial - Content
0. Basic Setup
1. Enable Google Cloud
2. Initialize Google Cloud
3. Setup Google Gemini
4. Streamlit Integration
5. Enhance Personality

## 0. Basic Setup
### [Visual Studio Code](https://code.visualstudio.com/)
You may also choose other develop tools that you prefer.
### [Python](https://www.python.org/downloads/)
make sure that your version is above 3.11
### Google Cloud Code
install this extension to connect your Google Cloud project

## 1. Enable Google Cloud
[Start](https://console.cloud.google.com/)

follow the instructions [here](https://cloud.google.com/cloud-console?utm_source=google&utm_medium=cpc&utm_campaign=na-US-all-en-dr-bkws-all-all-trial-e-dr-1707554&utm_content=text-ad-none-any-DEV_c-CRE_665735422256-ADGP_Hybrid%20%7C%20BKWS%20-%20MIX%20%7C%20Txt-Management%20Tools-Cloud%20Console-KWID_43700077225654741-kwd-55675752867&utm_term=KW_google%20cloud%20console-ST_google%20cloud%20console&gad_source=1&gclid=Cj0KCQiArrCvBhCNARIsAOkAGcXO2_affz2IH9q_ps1LDwrdsOe43AmOiJps1j9UK_ri0mnBWRd9eA0aApkNEALw_wcB&gclsrc=aw.ds)

## 2. Initialize Google Cloud
* setup the API server
<img width="1497" alt="Screen Shot 2024-03-12 at 12 33 03 PM" src="https://github.com/TommyCheng023/Gemini_Explorer/assets/115842289/c2fcfcd3-e879-458d-8fa7-90d6d4853cde">

* install and initialize SDK by typing the following command into the terminal
```sh
gcloud init
```
<img width="619" alt="Screen Shot 2024-03-09 at 2 04 59 PM" src="https://github.com/TommyCheng023/Gemini_Explorer/assets/115842289/a3042499-8630-4a83-8546-bda9806bdcb5">

* verifiy the configuration by typing the following command into the terminal
```sh
gcloud config list
```
<img width="542" alt="Screen Shot 2024-03-09 at 2 07 03 PM" src="https://github.com/TommyCheng023/Gemini_Explorer/assets/115842289/e185d15a-9d81-4f0e-a3b9-a33a5eb77a48">

* install required packages
```sh
pip install vertexai
```

* initialize vertexai project
```sh
import vertexai
from vertexai.preview import generative_models
from vertexai.preview.generative_models import GenerativeModel, Part, Content, ChatSession
project = "your-project-ID"
vertexai.init( project = project )
```
* create config and load model
```sh
config = generative_models.GenerationConfig( # add attributes you need )
model = GenerativeModel ( "gemini-pro", generation_config = config )
chat = model.start_chat()
```
## 3. Setup Google Gemini
* installation
```sh
pip install streamlit
```
* import package
```sh
import streamlit as st
```
* [Streamlit Guide](https://docs.streamlit.io/get-started)
  * We use `"Gemini-Pro"` by Google!
## 4. Streamlit Integration
* display and load chat history
* capture user input effortlessly
<img width="785" alt="Screen Shot 2024-03-11 at 5 38 13 PM" src="https://github.com/TommyCheng023/Gemini_Explorer/assets/115842289/8139eecd-633a-4de1-a5db-f34ba95304ec">

### Common Issue With Solutions
1. Any Runtime Error
solution: insert error-handling structures can avoid crashing your computer
```sh
try:
    # your code
except Exception as e:
    st.error(f"Issue Failed: {e}")
    st.stop()
```
2. Failed to send message or receive response: 503 DNS resolution failed for us-central1-aiplatform.googleapis.com:443: C-ares status is not ARES_SUCCESS qtype=SRV name=_grpclb._tcp.us-central1-aiplatform.googleapis.com: Timeout while contacting DNS servers
```sh
import os
os.environ['GRPC_DNS_RESOLVER'] = 'native'
```
## 5. Add Initial Message
### Initial Prompt
* enhance personality: This is something you can **define** your chatbot. Including what you want it to be called, what its style of chatting is going to be. All those requirements can be included in a string. 

<img width="1720" alt="Screen Shot 2024-03-11 at 2 09 51 PM" src="https://github.com/TommyCheng023/Gemini_Explorer/assets/115842289/978a6dc8-626a-4cbe-ba58-d86b805893de">

## Launch The App
```sh
streamlit run gemini_explorer.py
```
## Appendix
### Appreciation
* Appreciate Radical AI for providing such a precious experience on AI engineering.
* I also want to show my gratitude to Talha Sabri and Mikhail Ocampo for detailed instructions. :)

### About Contributors
* Xinyang(Tommy) Cheng
  * Personal Website: [About - Xinyang Cheng](https://tommycheng023.github.io/)
  * LinkedIn Profile: [Xinyang(Tommy) Cheng](www.linkedin.com/in/xinyang-cheng-325825260)
* [Project Report](https://www.loom.com/share/7908a19af79947acb34437baae798e81?sid=e0a07ad6-b9c0-4477-a010-67b5f2722dfe)
