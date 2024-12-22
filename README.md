# QnA ChatBot

This is a streamlined QnA chatbot application built with **Streamlit** and **LangChain Core**, powered by Groq AI models for natural language processing. It allows users to ask questions and get intelligent responses using various powerful LLMs (Large Language Models).

---

## Features

- **Dynamic Model Selection:** Choose from multiple Groq AI models based on your use case.
- **Adjustable Settings:** Customize temperature and maximum token length for response generation.
- **Interactive Interface:** Easy-to-use interface for asking questions and receiving answers in real time.
- **Integration with LangChain Core:** Seamlessly integrates prompting and output parsing for reliable response generation.

---

## Tech Stack

- **Streamlit**: For the interactive web interface.
- **LangChain Core**: For managing prompt templates and chaining LLMs.
- **Groq AI**: Backend for executing LLMs.
- **dotenv**: For secure environment variable management.

---

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/your-repo/Groq_Chatbot.git
   cd Groq_Chatbot
   

Create a .env file in the project directory and add the following keys:
.env
groq_api_key=your_groq_api_key
langchain_api_key=your_langchain_api_key


Run the application:
```bash
streamlit run app.py
