import os
import time
import streamlit as st
import random
from dotenv import load_dotenv
from together import Together

# Load API key
load_dotenv()
api_key = os.getenv("TOGETHER_API_KEY")
client = Together(api_key=api_key)

# Page setup
st.set_page_config(page_title="Chatbot", page_icon="🤖")

# Include custom fonts and styling
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;600&display=swap');
    @import url('https://fonts.googleapis.com/css2?family=Shadows+Into+Light&display=swap');
    @import url('https://fonts.googleapis.com/css2?family=Kalam:wght@400;700&display=swap');
    @import url('https://fonts.googleapis.com/css2?family=Nothing+You+Could+Do&display=swap');
    @import url('https://fonts.googleapis.com/css2?family=Indie+Flower&display=swap');
    
    .handwritten-font {
        font-family: 'Nothing You Could Do', 'Shadows Into Light', 'Indie Flower', 'Kalam', cursive !important;
        font-weight: 400;
        line-height: 1.3;
    }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown("<h1 style='text-align: center; font-family: \"Montserrat\", sans-serif;'> Autobot </h1>", unsafe_allow_html=True)

# Initialize session state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = [
        {"role": "system", "content": "You are a helpful AI assistant."}
    ]
    st.session_state.first_visit = True



# === Chat Input Section ===
user_input = st.chat_input("Type your message here...")

if user_input and user_input.strip():
    # Append and show user message instantly
    st.session_state.chat_history.append({"role": "user", "content": user_input})
    
    # This would normally trigger a rerun, but we'll handle it manually
    st.markdown(f"""
    <div style='display: flex; justify-content: flex-end; margin: 5px 0;'>
        <div style='background-color: #0084ff; color: white; padding: 10px;
                    border-radius: 10px; max-width: 80%;
                    font-family: "Montserrat", sans-serif; font-size: 17px;'>
            {user_input}
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Assistant typing placeholder
    assistant_response_placeholder = st.empty()

    with st.spinner("Thinking..."):
        response = client.chat.completions.create(
            model="meta-llama/Llama-3.3-70B-Instruct-Turbo-Free",
            messages=st.session_state.chat_history
        )
        result = response.choices[0].message.content

    # Typing effect for assistant response
    for i in range(1, len(result) + 1):
        assistant_response_placeholder.markdown(f"""
        <div style='display: flex; justify-content: flex-start; margin: 5px 0;'>
            <div style='background-color: #262525; color: white; padding: 10px;
                        border-radius: 10px; max-width: 80%;
                        font-family: "Montserrat", sans-serif; font-size: 17px;'>
                {result[:i]}
            </div>
        </div>
        """, unsafe_allow_html=True)
        time.sleep(0.01)  # Faster typing for better user experience

    # Save full assistant reply
    st.session_state.chat_history.append({"role": "assistant", "content": result})
    st.experimental_rerun()

# === Welcome Banner Section ===
if st.session_state.first_visit:
    welcome_variants = [
        ["Hey there! 👋", "I'm your AI sidekick.", "Ready when you are!"],
        ["Hi! 😊", "I’m here to make things easier.", "Ask me anything!"],
        ["Hello, friend! 🤗", "Let’s explore some ideas together.", "What’s on your mind?"],
        ["Greetings! 🚀", "This is your chatbot co-pilot speaking.", "How can I assist today?"],
        ["Yo! 😎", "Need help? I got you.", "Fire away!"],
    ]
    welcome_texts = random.choice(welcome_variants)


    welcome_placeholder = st.empty()
    
    # Container styling
    container_style = """
    <div style='text-align: center;
                color: white;
                padding: 25px;
                margin: 30px 0;'>
    """
    
    # Build and display each message character by character
    all_paragraphs = []
    
    for text in welcome_texts:
        current_paragraph = ""
        all_paragraphs.append("")
        
        # Character by character animation within each paragraph
        for char in text:
            # Add the next character
            current_paragraph += char
            all_paragraphs[-1] = current_paragraph
            
            # Format all paragraphs with proper styling
            formatted_content = ""
            for p in all_paragraphs:
                if p:  # Only include non-empty paragraphs
                    # Use a combination of inline style and class
                    formatted_content += f"""<p class="handwritten-font" 
                                        style='margin: 8px 0; 
                                            font-size: 24px;'>
                                        {p}
                                    </p>"""
            
            # Update the display
            welcome_placeholder.markdown(
                f"{container_style}{formatted_content}</div>",
                unsafe_allow_html=True
            )
            
            # Random slight variation in typing speed for natural effect
            typing_delay = 0.03 + (random.uniform(0, 0.01) + 0.02 * (char in ['.', '!', '?', ',']))
            time.sleep(typing_delay)
        
        # Add a slightly longer pause between paragraphs
        time.sleep(0.7)
    
    # Set first_visit to False so the animation doesn't play again
    st.session_state.first_visit = False

# === Chat Display ===
chat_container = st.container()
with chat_container:
    for message in st.session_state.chat_history:
        if message["role"] == "user":
            st.markdown(
                f"""
                <div style='display: flex; justify-content: flex-end; margin: 5px 0;'>
                    <div style='background-color: #0084ff; color: white; padding: 10px;
                                border-radius: 10px; max-width: 80%;
                                font-family: "Montserrat", sans-serif; font-size: 17px;'>
                        {message['content']}
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )
        elif message["role"] == "assistant":
            st.markdown(
                f"""
                <div style='display: flex; justify-content: flex-start; margin: 5px 0;'>
                    <div style='background-color: #262525; color: white; padding: 10px;
                                border-radius: 10px; max-width: 80%;
                                font-family: "Montserrat", sans-serif; font-size: 17px;'>
                        {message['content']}
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )

