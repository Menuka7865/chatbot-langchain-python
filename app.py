import os
import sys
from dotenv import load_dotenv
import google.generativeai as genai

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.messages import HumanMessage, AIMessage


def get_api_key() -> str:    
    load_dotenv()
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        print("Error: GEMINI_API_KEY not found in environment variables.")
        sys.exit(1)
    return api_key

def build_chatbot(modelName:str='gemini-2.0-flash',temperature:float = 0.7):
    api_key = get_api_key()
    genai.configure(api_key=api_key)
    
    chat_model = ChatGoogleGenerativeAI(model=modelName, temperature=temperature)
    message_history = ChatMessageHistory()
    
    return chat_model, message_history
    
def main():
    chat_model, message_history = build_chatbot()
    
    print("Chatbot is ready! Type 'exit' to quit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            break
        
        message_history.add_message(HumanMessage(content=user_input))
        response = chat_model.invoke(message_history.messages)
        message_history.add_message(AIMessage(content=response.content))
        
        print(f"Bot: {response.content}")


if __name__ == "__main__":
    main()