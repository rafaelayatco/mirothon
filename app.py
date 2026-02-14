import streamlit as st
import openai
import time

# --- CONFIG & API ---
# Replace with your key to stop placeholders: https://platform.openai.com/
API_KEY = "your-openai-api-key-here"

st.set_page_config(page_title="AVENIR | High Jewelry", page_icon="💎", layout="wide")

# Initialize Session States
if 'forged' not in st.session_state: st.session_state.forged = False
if 'image_url' not in st.session_state: st.session_state.image_url = ""
if 'messages' not in st.session_state: st.session_state.messages = []

# --- REGAL GOLD & DIAMOND CSS (FIXED SYNTAX) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@700;900&family=Playfair+Display:ital,wght@0,400;1,700&family=Inter:wght@200;400;600&display=swap');

    .stApp { background-color: #ffffff; color: #1a1a1a; font-family: 'Inter', sans-serif; }

    /* Diamond Banner */
    .diamond-banner {
        width: 100%;
        height: 480px;
        background-image: linear-gradient(rgba(0,0,0,0.4), rgba(0,0,0,0.2)), url('https://images.unsplash.com/photo-1573408302314-19273039c23d?q=80&w=2000');
        background-size: cover;
        background-position: center;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        border-bottom: 8px solid #d4af37;
    }

    /* Bold Huge Title */
    .avenir-title {
        font-family: 'Cinzel', serif;
        color: #ffffff;
        background: linear-gradient(to bottom, #ffffff 0%, #d4af37 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 11rem;
        font-weight: 900;
        letter-spacing: 35px;
        text-transform: uppercase;
        margin: 0;
        filter: drop-shadow(0 15px 30px rgba(0,0,0,0.6));
    }

    .tagline-regal {
        color: #ffffff;
        font-family: 'Inter', sans-serif;
        letter-spacing: 15px;
        text-transform: uppercase;
        font-size: 1.2rem;
        margin-top: -30px;
    }

    /* Input Card Overlay */
    .input-panel {
        background: #ffffff;
        padding: 50px;
        border: 1px solid #d4af37;
        margin-top: -100px;
        z-index: 100;
        position: relative;
        box-shadow: 0 40px 80px rgba(0,0,0,0.1);
    }

    /* Buttons */
    div.stButton > button {
        background: #1a1a1a;
        color: #d4af37 !important;
        border: 1px solid #d4af37;
        border-radius: 0px;
        padding: 20px;
        font-family: 'Cinzel', serif;
        font-weight: bold;
        letter-spacing: 4px;
        width: 100%;
        text-transform: uppercase;
    }

    div.stButton > button:hover {
        background: #d4af37;
        color: #ffffff !important;
    }

    .chat-bubble {
        background: #fdfaf4;
        border: 1px solid #d4af37;
        padding: 20px;
        margin-bottom: 15px;
        font-family: 'Playfair Display', serif;
        font-size: 1.1rem;
    }
    
    /* Clean Text Areas */
    .stTextArea textarea { border: 1px solid #d4af37 !important; border-radius: 0px !important; }
    </style>
    """, unsafe_allow_html=True)

# --- HEADER SECTION ---
st.markdown("""
    <div class="diamond-banner">
        <p class="avenir-title">AVENIR</p>
        <p class="tagline-regal">High Jewelry Atelier</p>
    </div>
    """, unsafe_allow_html=True)

# --- THE INPUT ATELIER ---
with st.container():
    st.markdown('<div class="input-panel">', unsafe_allow_html=True)
    
    with st.form("design_form"):
        left, right = st.columns([2, 1])
        with left:
            story = st.text_area("THE NARRATIVE", placeholder="Describe the memory you wish to immortalize...", height=180)
        with right:
            metal = st.selectbox("METAL", ["Polished Platinum", "18k Yellow Gold", "Champagne Gold"])
            style = st.selectbox("STYLE", ["Modernist", "Classical Heritage", "Organic Art"])
            forge_clicked = st.form_submit_button("FORGE MASTERPIECE")
    
    if forge_clicked and story:
        with st.spinner("Distilling your story into gold..."):
            try:
                if API_KEY != "your-openai-api-key-here":
                    client = openai.OpenAI(api_key=API_KEY)
                    response = client.images.generate(
                        model="dall-e-3",
                        prompt=f"Luxury {style} {metal} ring. Professional studio photography. Inspired by: {story}. White marble background, macro, 8k.",
                        size="1024x1024", quality="hd", n=1
                    )
                    st.session_state.image_url = response.data[0].url
                else:
                    # Fallback to a high-quality jewelry image if no API key is present
                    st.session_state.image_url = "https://images.unsplash.com/photo-1605100804763-247f67b3557e?q=80&w=1000"
                
                st.session_state.forged = True
            except Exception as e:
                st.error(f"Generation failed: {e}")
    
    st.markdown('</div>', unsafe_allow_html=True)

# --- THE REVEAL & AI CONCIERGE ---
if st.session_state.forged:
    st.markdown("<br><br>", unsafe_allow_html=True)
    col_img, col_chat = st.columns([1, 1])
    
    with col_img:
        st.image(st.session_state.image_url, caption="AVENIR EXCLUSIVE DESIGN", use_container_width=True)
    
    with col_chat:
        st.markdown("### <span style='color:#b38728; font-family:Cinzel;'>Proposal Concierge</span>", unsafe_allow_html=True)
        st.markdown('<div class="chat-bubble"><b>Avenir:</b> Your design is complete. I am here to help you plan the moment you present it. Should we discuss a script or a location?</div>', unsafe_allow_html=True)
        
        # Simple Chat History
        for m in st.session_state.messages:
            st.markdown(f'<div style="text-align:right; color:#888; margin-bottom:10px;"><i>You: {m}</i></div>', unsafe_allow_html=True)
        
        with st.form("chat_input_form", clear_on_submit=True):
            user_msg = st.text_input("Message your private consultant...")
            if st.form_submit_button("BOOK PRIVATE CONSULTATION"):
                if user_msg:
                    st.session_state.messages.append(user_msg)
                    st.rerun()
