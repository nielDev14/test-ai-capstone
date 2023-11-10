from dotenv import load_dotenv
import os

from langchain.chat_models import ChatGooglePalm
from langchain.schema import (
  SystemMessage,
  HumanMessage,
  AIMessage
)

def main():
  load_dotenv()
  #test api 
  if os.getenv("GOOGLE_API_KEY") is None:
    print("Please set GOOGLE_API_KEY")
    exit(1)
  else:
    print("GOOGLE_API_KEY is set")  
  
  chat = ChatGooglePalm(temperature=0.5, model_name ="models/chat-bison-001")
  messages = [
    SystemMessage(content="You are a helpful AI assistant."),
  ] 
  
  print("Hello I am a helpful AI assistant.")
  
  while True:
    user_input = input("You: ")
    
    messages.append(HumanMessage(content=user_input))
    
    ai_response = chat(messages)
    
    messages.append(AIMessage(content=ai_response.content))
    
    print("\nAssistant:\n", ai_response.content)
  
  
  
if __name__ == '__main__':
  main()