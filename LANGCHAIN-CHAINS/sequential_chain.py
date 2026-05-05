from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv, parser
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()


prompt1 = PromptTemplate(
    template='generate a detailed plan to learn {topic} in 3 months',
    input_variables=['topic']
)
prompt2 = PromptTemplate(
    template='What are the best resources to learn {topic}?',
    input_variables=['topic']
)

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0)

parser = StrOutputParser()

chain = prompt1 | model | parser | prompt2 | model | parser

result = chain.invoke({'topic': 'Python programming'})

print(result)
