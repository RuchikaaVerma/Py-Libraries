from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

import streamlit as st
load_dotenv()
model=ChatOpenAI()

while True:
    user_input=input("You: ")
    if user_input.lower() in ["exit", "quit"]:
        print("Exiting the chatbot. Goodbye!")
        break
    result=model.invoke(user_input)