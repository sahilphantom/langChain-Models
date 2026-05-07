from langchain_community.document_loaders import TextLoader

loader = TextLoader('example.txt', encoding='utf-8')

documents = loader.load()
