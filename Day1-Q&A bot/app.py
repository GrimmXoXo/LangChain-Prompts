#Q&A Chatbots
from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
import os
from dotenv import load_dotenv

load_dotenv()

import streamlit as st


def get_openai_response(question):
    llm=OpenAI(openai_api_key=os.getenv('OPENAI_API_KEY'),model_name='text-davinci-003',temperature=0.6)
    response=llm(question)
    return response

def sentiment_analysis(sentiment):
    llm=ChatOpenAI(openai_api_key=os.getenv('OPENAI_API_KEY'),model_name='gpt-3.5-turbo',temperature=0.6)
    result=llm.predict(f'Give me sentiment analysis in one word for this statement which i am going to type now:   {sentiment}')
    return result


#StreamLit

st.set_page_config(page_title='Q&A Chatbot,Sentiment Analysis')

st.header('Langchain Application')


input=st.text_input('Input: ',key='input')
response=get_openai_response(input)


submit=st.button('The Response is')

input2=st.text_input('Input2: ',key='input2')
response2=sentiment_analysis(input2)
submit2=st.button('The answer is')



if submit:
    st.subheader('The response is: ')
    st.write(response)

if submit2:
    st.subheader('The sentiment is')
    st.write(response2)
