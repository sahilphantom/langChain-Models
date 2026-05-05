from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv


load_dotenv()

chat = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

result = chat.invoke("what is the capital of pakistan")
print(result.content)
