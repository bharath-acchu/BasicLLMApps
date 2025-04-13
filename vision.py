from dotenv import load_dotenv
load_dotenv() ## its used to load the env variables

import streamlit as st
import os
import google.generativeai as genai
import pathlib
import textwrap
from PIL import Image


## api key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


## model initialise
model = genai.GenerativeModel('gemini-2.0-flash')

def get_gemini_response(input,image):
    if input !="":
        response = model.generate_content([input,image])
    else:
        response = model.generate_content(image)
    return response.text


st.set_page_config(page_title="Gemini image demo")

st.header("Basic LLM app using Gemini")

input=st.text_input("Input prompt: ",key="input")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
image = ""

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.", use_column_width=True)



submit=st.button("Tell about the image")

## If submit button is clicked

if submit: 
    response=get_gemini_response(input,image)
    st.subheader("The Response is")
    st.write(response)

