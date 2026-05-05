from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()


prompt = PromptTemplate(
    template='What is the capital of France?',
    input_variables=['topic']
)

model = ChatOpenAI(model='gpt-3.5-turbo', temperature=0)

chain = prompt | model | StrOutputParser()

result = chain.invoke({'topic': 'France'})

print(result)
