from langchain_google_genai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding = OpenAIEmbeddings(model='text-embedding-3-large', dimension=32)

documents = [
    "hagdajhgdsahdgjagdajsg",
    "akjsdhjshdjshdjshdjsdhjs",
    "jashdjshdjshdsjdhjshdsjhdjshd"
]

result = embedding.embed_documents(documents)

print(str(result))
