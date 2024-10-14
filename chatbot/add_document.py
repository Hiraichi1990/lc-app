import os
import sys
import pinecone
from dotenv import load_dotenv
from langchain_community.document_loaders import UnstructuredFileLoader
from langchain_openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.vectorstores import Pinecone

load_dotenv()

# Pinecone を LangChain のベクターストアとして使用する
def initialize_vectorstore():
    pinecone.init(
        pinecone_api_key = os.environ["PINECONE_API_KEY"],
        environment = os.environ["PINECONE_ENV"],
    )
    
    index_name = os.environ["PINECONE_INDEX"]
    embeddings = OpenAIEmbemddings()
    return Pinecone.from_exisiting_index(index_nema, embeddings)

# 以下メイン処理
if _name_ == "_main_":
    file_name = sys.argv[1]
    loader = UnstructuredFileLoader(file_path)
    raw_docs = loader.load()
    
    text_splitter = CharacterTextSplitter(chunk_size=300, chunk_overlap=30)
    docks= text_splitter.split_documents(raw_docs)
    
    vectorstore = initialize_vectorstore()
    vectorstore.add_documents(docs)