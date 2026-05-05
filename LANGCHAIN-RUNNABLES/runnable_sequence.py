from langchain_google_genai import ChatGoogleGenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableSequence
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenAI(model='gemini-2.5-flash', temperature=0.7)
parser = StrOutputParser()
prompt1 = PromptTemplate(
    template='What is the capital of {topic}',
    input_variables=['topic']
)

chain = RunnableSequence(prompt1 | model | parser)

result = chain.invoke({'topic': 'France'})

print(result)
