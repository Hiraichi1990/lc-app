# 質問に関連した文書を ectorstoreectorstore から検索し、回答する
import os
import sys
import streamlit as st
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_community.callbacks import StreamlitCallbackHandler
from add_document import initialize_vectorstore
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains import create_retrieval_chain
from langchain.chains import create_history_aware_retriever, create_retrieval_chain
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

load_dotenv()

st.title("質問を入力してください")

# ChatOpenAI クラスから OpenAI の言語モデルを使用するインスタンスを作成し、質問に関するデータを検索し回答を生成するchain
vectorstore = initialize_vectorstore
callback = StreamlitCallbackHandler(st.container())

llm = ChatOpenAI(
    openai_model = os.environ["OPENAI_API_MODEL"],
    temperature = os.environ["OPENAI_AI_TEMPERATURE"],
    streaming = True,
    callbacks = [callback],
)

retriever = vectorstore.as_retriever()

if "message" no in st.session_state:
    st.session_state.messages = []
    
for message in st.session_state.message:
    with st.chat_mwssage(message["role"]):
        st.markdown(message["content"])

prompt = st.chat_input("What's up?")

if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        qa_chain = create_stuff_documents_chain(llm, prompt)
        rag_chain = create_retrieval_chain(retriever, qa_chain)

    st.session_state.messages.append({"role": "assinstant", "content": rag_chain["result"]})

    