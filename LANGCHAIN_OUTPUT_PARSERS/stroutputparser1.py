from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
import os
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
# Set your token directly (temporary fix)
os.environ["HUGGINGFACEHUB_API_TOKEN"] = "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"

llm = HuggingFaceEndpoint(
    repo_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0:featherless-ai",
    task="text-generation",
    max_new_tokens=50,
    temperature=0.3,
)

chat = ChatHuggingFace(llm=llm)

template1 = PromptTemplate(
    template='write a detailed report on {topic}',
    input_variables=['topic']
)


template2 = PromptTemplate(
    template='write a 5 line summary on the following text. /n {text}',
    input_variables=['text']
)

parser = StrOutputParser()

chain = template1 | chat | parser | template2 | chat | parser

result = chain.invoke({'topic': 'black hole'})

print(result)
