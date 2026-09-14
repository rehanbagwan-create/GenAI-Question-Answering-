from dotenv import load_dotenv
load_dotenv()

from langchain_groq import ChatGroq
import streamlit as st 

llm = ChatGroq(model="openai/gpt-oss-20b",temperature=0)

st.title ("🤖 GenAI Q&A Assistant")
st.markdown (
    """ **Your intelligent AI assistant for questions, answers, and learning.**
    
        Ask a question below and let GenAI provide you with a clear and helpful answer.  
        Built with **LangChain** and **Streamlit**."""
)


if "message"  not in st.session_state :
    st.session_state.message =[]


for message in st.session_state.message :
    role =message ["role"]
    content =message ["content"]
    st.chat_message(role).markdown(content)




question = st.chat_input("Ask Anything ?")

if question:
    st.session_state.message.append ({"role": "user", "content":question})
    st.chat_message ("user").markdown(question)
    result = llm.invoke(question)
    st.chat_message("ai").markdown(result.content)
    st.session_state.message.append({"role":"ai","content": result.content}) 


