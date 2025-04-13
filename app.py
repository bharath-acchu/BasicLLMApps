from dotenv import load_dotenv
load_dotenv() ## its used to load the env variables

import streamlit as st
import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

## function to load gemini pro model
model = genai.GenerativeModel('gemini-2.0-flash')


def get_gemini_response(question):
    response = model.generate_content(question)
    return response.text


st.set_page_config(page_title="Q&A")

st.header("Basic LLM app using Gemini")

input=st.text_input("Input: ",key="input")


submit=st.button("Ask the question")

## If ask button is clicked

if submit:
    
    response=get_gemini_response(input)
    st.subheader("The Response is")
    st.write(response)
