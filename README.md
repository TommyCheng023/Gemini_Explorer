# Gemini_Explorer
## Description
A Streamlit APP of an AI chat interface taking `Gemini` as an API accessed by a personal Google Cloud account. 
## Demo Video
<ins>coming soon</ins>

## Tutorial - Content
0. Basic Setup
1. Enable Google Cloud
2. Initialize Google Cloud
3. Setup Google Gemini
4. Streamlit Integration
5. Add Initial Message

## 0. Basic Setup
### Python
make sure that your version is above 3.11


## 1. Enable Google Cloud
follow the instructions [here](https://cloud.google.com/cloud-console?utm_source=google&utm_medium=cpc&utm_campaign=na-US-all-en-dr-bkws-all-all-trial-e-dr-1707554&utm_content=text-ad-none-any-DEV_c-CRE_665735422256-ADGP_Hybrid%20%7C%20BKWS%20-%20MIX%20%7C%20Txt-Management%20Tools-Cloud%20Console-KWID_43700077225654741-kwd-55675752867&utm_term=KW_google%20cloud%20console-ST_google%20cloud%20console&gad_source=1&gclid=Cj0KCQiArrCvBhCNARIsAOkAGcXO2_affz2IH9q_ps1LDwrdsOe43AmOiJps1j9UK_ri0mnBWRd9eA0aApkNEALw_wcB&gclsrc=aw.ds)

## 2. Initialize Google Cloud
* initialize SDK by typing the following command into the terminal
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
## 3. Setup Google Gemini
* installation
```sh
pip install streamlit
```
* verification
```sh
streamlit hello
```
* [Streamlit Guide](https://docs.streamlit.io/get-started)
  * We use `"Gemini-Pro"` by Google!
## 4. Streamlit Integration
* write a helper function
  * `llm_function`: a function used to display and send streamlit messages
## 5. Add Initial Message
* let the AI speaks first
  * simply define a `String` containing an initial prompt and pass it into the `llm_function`
## Launch The App
```sh
streamlit run gemini_explorer.py
```
## Appendix
### Appreciation
* Thanks for RadicalX providing such a precious experience on AI engineering.
* I also want to show my gratitude to Talha Sabri and Mikhail Ocampo for detailed instructions. :)

### About Contributors
* Xinyang(Tommy) Cheng
  * Personal Website: [About - Xinyang Cheng](https://tommycheng023.github.io/)
  * LinkedIn Profile: [Xinyang(Tommy) Cheng](www.linkedin.com/in/xinyang-cheng-325825260)
