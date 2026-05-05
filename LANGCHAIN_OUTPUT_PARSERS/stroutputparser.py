from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
import os
from langchain_core.prompts import PromptTemplate

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

prompt1 = template1.invoke({'topic': 'black hole'})

result = chat.invoke(prompt1)

prompt2 = template2.invoke({'text': result.content})

result1 = chat.invoke(prompt2)

print(result1.content)
