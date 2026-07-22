import streamlit as st
import google.generativeai as genai

# Page setup
st.set_page_config(page_title="Study Buddy - AI Chatbot", page_icon="📚")
st.title("📚 Study Buddy - Tumcha AI Mitra")
st.write("Kuthla hi prashna vichara, notes summarize kara, kinwa doubts clear kara!")

# Sidebar madhe API Key
with st.sidebar:
    st.header("Settings")
    api_key = st.text_input("Tumchi Google AI API Key takha", type="password")
    st.markdown("[API Key kuthun milvel?](https://aistudio.google.com/app/apikey)")

if api_key:
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-1.5-flash')

    # Chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Magche messages dakhav
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # User input
    if prompt := st.chat_input("Ithe prashna liha... udaharan: 'Photosynthesis samjaun sang'"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        # AI cha uttar
        with st.chat_message("assistant"):
            with st.spinner("Vichar karat aahe..."):
                response = model.generate_content(f"Tumhi ek helpful AI teacher ahat. Marathi aani English mix karun sopa bhashet uttar dya. Prashna: {prompt}")
                st.markdown(response.text)
        st.session_state.messages.append({"role": "assistant", "content": response.text})
else:
    st.warning("Krupaya sidebar madhe tumchi API Key taka")
