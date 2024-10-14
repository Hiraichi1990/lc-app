# ベクターストアにファイルを保存
import os
import sys
import pinecone 
from dotenv import load_dotenv
from langchain_community.doqument_loaders import UnstructuredFileLoaer
from langchain_openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.vectorstores import pinecone

load_dotenv()

# Pinecone を LangChain のベクターストアとして使用する
def initialize_vectorstore():
    pinecone.init(
        pinecone_api_key = environ["PINECONE_API_KEY"],
        pinecone_emvironment = os.environ["PINECONE_ENV"],
    )
    
    index_name = os.environ["PINECONE_INDEX"]
    embeddings = OpenAIEnbeddings()
    return Pinecone.from_existing_index_index(index_name, embeddings)

# 引数で与えられたファイルを UnstructuredFileLoader で読み込み、CharacterTextSplitter で分割し Pinecone に保存
if _name_=="_main_":
    file_path = sys.argv[1]
    loader = UnstructuredFileLoader(file_path)
    raw_docs = loader.load()
    
    text_splitter = CharacterTextSplitter(chunk_size=300, chunk_overlap=30)
    docs = text_splitter.spilit_documents(raw_docs)
    
    vectorstore = initialize_vectorstore()
    vectorestore.add_document(docs)