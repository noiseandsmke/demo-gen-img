import streamlit as st
from gen_img import reqGenImg

def main():
    # app config
    st.set_page_config(page_title="Demo", layout='wide', page_icon='🔥')
    # chat history
    if 'chat_history' not in st.session_state:
        st.session_state.chat_history = [{"role":"ai", "content": "Hello I'm an AI image bot. How can I help you?"}]
    # user input
    user_prompt = st.chat_input("Type your prompt for generating image...")
    if user_prompt is not None:
        # Add user's prompt to chat history
        st.session_state.chat_history.append({"role": "user", "content": user_prompt})
        image_url = reqGenImg(user_prompt)
        # image_url = imageURL
        # Add AI's response (image) to chat history
        st.session_state.chat_history.append({"role": "ai", "content": image_url})
    # Display conversation
    for message in st.session_state.chat_history:
        if message["role"] == "user":
            with st.chat_message("Human"):
                st.markdown(message["content"])
        elif message["role"] == "ai":
            with st.chat_message("AI"):
                content = message["content"]
                if content.startswith('http'):
                    st.image(content, use_column_width=True)
                else:
                    st.markdown(content)
    # sidebar
    with st.sidebar:
        st.title('Image Generation 🤖')
        st.markdown('''
            An AI-powered Image Generation ChatBot built using:
            - [Streamlit](https://streamlit.io)
            - [LimeWire AI API](https://www.limewire.com/ai-api)
                    ''')
        st.subheader('©️HCMUTE')

if __name__ == "__main__":
    main()
