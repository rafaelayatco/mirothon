import streamlit as st
import openai
import time

# --- MANDATORY SETUP ---
# To stop placeholders, you MUST put your key here:
# Get one at: https://platform.openai.com/
API_KEY = "PASTE_YOUR_OPENAI_KEY_HERE"

# --- PAGE SETUP ---
st.set_page_config(page_title="AVENIR | High Jewelry", page_icon="💍", layout="wide")

# Initialize Session States
if 'image_url' not in st.session_state: st.session_state.image_url = None
if 'chat_history' not in st.session_state: st.session_state.chat_history = []
if 'step' not in st.session_state: st.session_state.step = "input"

# --- REGAL WHITE & GOLD CSS ---
st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@700;900&family=Inter:wght@300;600&display=swap');

    .stApp {{ background-color: #ffffff; }}

    /* Diamond Banner */
    .hero-banner {{
        background: linear-gradient(rgba(0,0,0,0.4), rgba(0,0,0,0.4)), 
                    url('https://images.unsplash.com/photo-1573408302314-19273039c23d?q=80&w=2000');
        background-size: cover;
        background-position: center;
        height: 400px;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        border-bottom: 5px solid #d4af37;
    }}

    /* Massive Bold Title */
    .avenir-logo {{
        font-family: 'Cinzel', serif;
        font-size: 10rem;
        font-weight: 900;
        letter-spacing: 25px;
        color: #ffffff;
        background: linear-gradient(to bottom, #f1d38e, #b38728);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin: 0;
        text-transform: uppercase;
        filter: drop-shadow(0 10px 20px rgba(0,0,0,0.5));
    }

    /* Input Rectangle */
    .input-box {{
        background: white;
        padding: 50px;
        border: 1px solid #d4af37;
        margin-top: -80px;
        box-shadow: 0 30px 60px rgba(0,0,0,0.1);
        position: relative;
        z-index: 10;
    }}

    /* Gold Buttons */
    div.stButton > button {{
        background: #1a1a1a;
        color: #d4af37 !important;
        border: 1px solid #d4af37;
        border-radius: 0px;
        font-family: 'Cinzel', serif;
        font-weight: bold;
        padding: 20px;
        width: 100%;
        text-transform: uppercase;
        letter-spacing: 2px;
    }}

    div.stButton > button:hover {{
        background: #d4af37;
        color: white !important;
    }}

    .chat-bubble {{
        background: #fdfaf4;
        border-left: 3px solid #d4af37;
        padding: 15px;
        margin: 10px 0;
    }}
    </style>
    """, unsafe_allow_html=True)

# --- BANNER ---
st.markdown('<div class="hero-banner"><h1 class="avenir-logo">AVENIR</h1><p style="color:white; letter-spacing:8px;">HIGH JEWELRY ATELIER</p></div>', unsafe_allow_html=True)

# --- THE PROCESS ---
if st.session_state.step == "input":
    with st.container():
        st.markdown('<div class="input-box">', unsafe_allow_html=True)
        col1, col2 = st.columns([2,1])
        with col1:
            story = st.text_area("SHARE YOUR NARRATIVE", placeholder="A winter night in Paris...", height=150)
        with col2:
            metal = st.selectbox("METAL", ["18k White Gold", "Champagne Gold", "Platinum"])
            forge = st.button("Forge Design")
        st.markdown('</div>', unsafe_allow_html=True)

    if forge:
        if API_KEY == "PASTE_YOUR_OPENAI_KEY_HERE":
            st.error("⚠️ SYSTEM ERROR: You must paste an OpenAI API Key into the code to generate the real image.")
        elif story:
            with st.spinner("The AI Goldsmith is crafting..."):
                try:
                    client = openai.OpenAI(api_key=API_KEY)
                    # This is the "Proper" generation call
                    response = client.images.generate(
                        model="dall-e-3",
                        prompt=f"Luxury {metal} jewelry design. High-end product photography. Inspired by: {story}. White marble background, macro lens, 8k, cinematic lighting.",
                        size="1024x1024", n=1
                    )
                    st.session_state.image_url = response.data[0].url
                    st.session_state.step = "reveal"
                    st.rerun()
                except Exception as e:
                    st.error(f"Generation failed: {e}")

# --- THE REVEAL & CHAT ---
elif st.session_state.step == "reveal":
    col_img, col_chat = st.columns([1, 1])
    
    with col_img:
        st.image(st.session_state.image_url, use_container_width=True)
        if st.button("New Design"):
            st.session_state.step = "input"
            st.rerun()

    with col_chat:
        st.markdown("### <span style='color:#b38728; font-family:Cinzel;'>THE CONCIERGE</span>", unsafe_allow_html=True)
        
        # Chat Interface
        for chat in st.session_state.chat_history:
            st.markdown(f'<div class="chat-bubble">{chat}</div>', unsafe_allow_html=True)
            
        with st.form("chat_form", clear_on_submit=True):
            user_msg = st.text_input("Ask about your proposal...")
            send = st.form_submit_button("BOOK PRIVATE CONSULTATION")
            
            if send and user_msg:
                st.session_state.chat_history.append(f"**You:** {user_msg}")
                st.session_state.chat_history.append("**Avenir:** Based on your design, I suggest a candlelit evening. Would you like a specific script?")
                st.rerun()
