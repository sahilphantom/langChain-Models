from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
import os
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
# Set your token directly (temporary fix)
os.environ["HUGGINGFACEHUB_API_TOKEN"] = "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"

llm = HuggingFaceEndpoint(
    repo_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0:featherless-ai",
    task="text-generation",
    max_new_tokens=50,
    temperature=0.3,
)

chat = ChatHuggingFace(llm=llm)

parser = JsonOutputParser()

template = PromptTemplate(
    template='give me the name, age, and city of a fictional person \n {format_instruction}',
    input_variables=[],
    partial_variables={'format_instruction': parser.get_format_instructions()}
)

chain = template | chat | parser

result = chain.invoke({})

print(result)
