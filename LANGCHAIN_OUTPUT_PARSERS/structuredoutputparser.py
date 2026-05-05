from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
import os
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StructuredOutputParser, ResponseSchema
# Set your token directly (temporary fix)
os.environ["HUGGINGFACEHUB_API_TOKEN"] = "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"

llm = HuggingFaceEndpoint(
    repo_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0:featherless-ai",
    task="text-generation",
    max_new_tokens=50,
    temperature=0.3,
)

chat = ChatHuggingFace(llm=llm)

schema = {
    ResponseSchema(
        name="name", description="The name of the person", type="string"),
    ResponseSchema(
        name="age", description="The age of the person", type="integer"),
    ResponseSchema(
        name="city", description="The city of the person", type="string"),

}

parser = StructuredOutputParser.from_response_schemas(schema)

template = PromptTemplate(
    template='give me 3 fact about {topic} \n {format_instruction}',
    input_variables=['topic'],
    partial_variables={'format_instruction': parser.get_format_instructions()}
)

chain = template | chat | parser

result = chain.invoke({'topic': 'black hole'})

print(result)
