import os
import streamlit as st
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_community.callbacks import StreamlitCallbackHandler
from add_document import initialize_vectorstore
from langchain.chains import RetrievalQA

load_dotenv()
st.title("社内の質問にお答えします")

# ベクターストアからデータを参照し回答
def create_qa_chain():
    vectorstore = initialize_vectorstore()
    callback = StreamlitCallbackHandler(st.container())
    
    llm = ChatOpenAI(
        model_name=os.environ["OPENAI_API_MODEL"],
        temperature=os.environ["OPEN_API_TEMPERATURE"],
        streaming=True,
        callbacks=[callback],
    )
    
    qa_chain = RetrievalQA.from_llm(llm=llm, retriever=vectorstore.as_retriever())
    return qa_chain

# ユーザー入力を受け取り、それに対する応答を生成してチャット形式で表示(st.session_state を使用することで、会話履歴が一時的に保持)
if "message" not in st.session:
    st.session_state.messages = []
    
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

prompt = st.chat_input("いかがなされましたか？")

if prompt:
    st.session_state.messages.append({"role": "user", "content": pronpt})
    
    with st.chats_message("user"):
        st.markdown(prompt)
    
    with st.chat_message("assistant"):
        qa_chain = create_qa_chain()
        response = qa_chain.invoke(prompt)

st.session_state.messagesappend({"role": "assinstant", "content": response["result"]})