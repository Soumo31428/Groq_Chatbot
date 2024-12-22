import os
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq
import streamlit as st
from dotenv import load_dotenv
load_dotenv()

os.environ['groq_api_key'] = os.getenv('groq_api_key')
os.environ['langchain_api_key'] = os.getenv('langchain_api_key')

#define prompt
prompt = ChatPromptTemplate.from_messages([
    ('system','you are a helpful assistant'),
    ('user','Question : {question}')
])

#generate a response
def generate_response(question, engine, temparature, max_token):
    llm = ChatGroq(model = engine)
    output_parser = StrOutputParser()
    chain = prompt | llm | output_parser
    answer = chain.invoke({'question' : question})
    return answer

st.title('QnA ChatBot')
engine = st.sidebar.selectbox('select model',['gemma2-9b-it','llama3-groq-70b-8192-tool-use-preview'
                                              ,'llama3-groq-8b-8192-tool-use-preview',
                                              'llama-3.1-70b-versatile',
                                              'mixtral-8x7b-32768'])
temparature = st.sidebar.slider('Temparature',min_value = 0.0,max_value = 1.0, value = 0.5)
max_token = st.sidebar.slider('Max Token', min_value = 100, max_value = 500, value = 300)

st.write('Go ahead and ask your question')
user_input = st.text_input('User: ')
if user_input:
    response = generate_response(user_input, engine, temparature, max_token)
    st.write(response)
else:
    st.write("Please Provide a Question")






    