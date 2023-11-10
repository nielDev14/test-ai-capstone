from dotenv import load_dotenv
import os

from langchain.chat_models import ChatGooglePalm
from langchain.chains import ConversationChain
from langchain.memory import ConversationEntityMemory
from langchain.memory.prompt import   ENTITY_MEMORY_CONVERSATION_TEMPLATE

def main():
  load_dotenv()
  #test api 
  if os.getenv("GOOGLE_API_KEY") is None:
    print("Please set GOOGLE_API_KEY")
    exit(1)
  else:
    print("GOOGLE_API_KEY is set")  
  
  llm = ChatGooglePalm(temperature=0.5, model_name ="models/chat-bison-001")
  
  conversation = ConversationChain(
    llm = llm,
    memory = ConversationEntityMemory(llm = llm),
    prompt= ENTITY_MEMORY_CONVERSATION_TEMPLATE,
    verbose= False
    )
  
  print("Hello I am a helpful AI assistant.")
  
  while True:
    user_input = input("\nYou: ")
    
    ai_response = conversation.predict(input = user_input)
    
    print("\nAssistant:\n", ai_response)
  
  
  
if __name__ == '__main__':
  main()