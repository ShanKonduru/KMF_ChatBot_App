import streamlit as st
from dotenv import load_dotenv



def launch_chat_bot():
    print('I am in Launch Chat Bot')
    st.set_page_config(page_title="Knowledge Management Framework (KMF) ChatBot App", page_icon=":books:")
    st.header("Knowledge Management Framework (KMF) ChatBot :books:")
    st.text_input("Ask any question about Railway Domain KmfChatBot :robot_face:")
    
    with st.sidebar:
        st.subheader("Your documents")
        st.file_uploader("Upload Railway Domain related KMF documents :books: here.. click 'Process Files'")
        if (st.button("Process Files")):
            
        
    
    


if __name__ == "__main__":
    load_dotenv()
    launch_chat_bot()
