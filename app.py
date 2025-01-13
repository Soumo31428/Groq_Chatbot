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
                                              'mixtral-8x7b-32768'],
                                              help="Choose a model based on your needs. Larger models may provide more detailed answers."
                                              )
temparature = st.sidebar.slider('Temparature',min_value = 0.0,max_value = 1.0, value = 0.5)
max_token = st.sidebar.slider('Max Token', min_value = 100, max_value = 500, value = 300)

# Input box for user question
st.write('Ask your question:')
user_input = st.text_input('User:', placeholder="Type your question here...")
clear_button = st.button("Clear Input")

if clear_button:
    user_input = ""  # Clear input

if user_input:
    with st.spinner('Generating response...'):
        response = generate_response(user_input, engine, temparature, max_token)
    st.write('Response:')
    st.markdown(f'<div style="padding:10px; border-radius:5px;">{response}</div>', unsafe_allow_html=True)

    # Feedback options
    st.write("Was this response helpful?")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("👍 Helpful"):
            st.success("Thanks for your feedback!")
    with col2:
        if st.button("👎 Not Helpful"):
            st.warning("Thanks! We'll work on improving day by day.")
else:
    st.write("Please provide a question to get started.")






    





    
