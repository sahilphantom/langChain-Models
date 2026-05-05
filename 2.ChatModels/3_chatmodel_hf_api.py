from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
import os

# Set your token directly (temporary fix)
os.environ["HUGGINGFACEHUB_API_TOKEN"] = "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"

llm = HuggingFaceEndpoint(
    repo_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0:featherless-ai",
    task="text-generation",
    max_new_tokens=50,
    temperature=0.3,
)

chat = ChatHuggingFace(llm=llm)

result = chat.invoke("what is the capital of pakistan")
print(result.content)
