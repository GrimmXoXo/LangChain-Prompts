#Q&A Chatbots
from langchain.llms import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

import streamlit as st

def get_openai_response(question):
    llm=OpenAI(openai_api_key=os.getenv('OPENAI_API_KEY'),model_name='text-davinci-003',temperature=0.6)
    response=llm(question)
    return response



#StreamLit

st.set_page_config(page_title='Q&A Chatbot')

st.header('Langchain Application')


input=st.text_input('Input: ',key='input')
response=get_openai_response(input)


submit=st.button('The Response is')

if submit:
    st.subheader('The response is: ')
    st.write(response)

