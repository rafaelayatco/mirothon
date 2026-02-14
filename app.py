import streamlit as st
import time

# --- CONFIG ---
st.set_page_config(page_title="Avenir | Bold Luxury", page_icon="💎", layout="wide")

# --- SESSION STATE (The "Memory" of your app) ---
if 'forged' not in st.session_state:
    st.session_state.forged = False
if 'chat_mode' not in st.session_state:
    st.session_state.chat_mode = False
if 'messages' not in st.session_state:
    st.session_state.messages = []

# --- REGAL GOLD & DIAMOND CSS ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@700;900&family=Playfair+Display:ital,wght@0,400;1,700&family=Inter:wght@200;400;600&display=swap');

    .stApp { background-color: #ffffff; color: #1a1a1a; font-family: 'Inter', sans-serif; }

    /* Diamond Banner */
    .diamond-banner {
        width: 100%;
        height: 450px;
        background-image: linear-gradient(rgba(0,0,0,0.3), rgba(0,0,0,0.3)), url('https://images.unsplash.com/photo-1573408302314-19273039c23d?q=80&w=2000');
        background-size: cover;
        background-position: center;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        border-bottom: 5px solid #d4af37;
    }

    /* Bold Avenir Title */
    .avenir-title {
        font-family: 'Cinzel', serif;
        color: #ffffff;
        background: linear-gradient(to bottom, #ffffff 0%, #d4af37 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 10rem; /* Bold and Big */
        font-weight: 900;
        letter-spacing: 25px;
        text-transform: uppercase;
        margin: 0;
        filter: drop-shadow(0 10px 20px rgba(0,0,0,0.5));
    }

    .tagline-regal {
        color: #ffffff;
        font-family: 'Inter', sans-serif;
        letter-spacing: 10px;
        text-transform: uppercase;
        font-size: 1rem;
        font-weight: 400;
        margin-top: -20px;
    }

    /* Floating Input Box */
    .input-panel {
        background: #ffffff;
        padding: 50px;
        border: 1px solid #e0e0e0;
        margin-top: -100px;
        z-index: 100;
        position: relative;
        box-shadow: 0 30px 60px rgba(0,0,0,0.1);
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
        letter-spacing: 3px;
        width: 100%;
        transition: 0.4s ease;
    }

    div.stButton > button:hover {
        background: #d4af37;
        color: #ffffff !important;
    }

    /* AI Chat Bubble Interface */
    .chat-window {
        background: #fdfaf4;
        border: 1px solid #eee;
        padding: 20px;
        height: 400px;
        overflow-y: auto;
        border-radius: 4px;
        margin-bottom: 15px;
    }

    .bot-msg { color: #b38728; font-family: 'Playfair Display', serif; font-size: 1.1rem; margin-bottom: 10px; }
    .user-msg { color: #555; font-family: 'Inter', sans-serif; font-size: 0.9rem; text-align: right; margin-bottom: 10px; }

    </style>
    """, unsafe_allow_html=True)

# --- BANNER ---
st.markdown("""
    <div class="diamond-banner">
        <p class="avenir-title">AVENIR</p>
        <p class="tagline-regal">The Future of High Jewelry</p>
    </div>
    """, unsafe_allow_html=True)

# --- MAIN ATELIER ---
with st.container():
    st.markdown('<div class="input-panel">', unsafe_allow_html=True)
    
    with st.form("design_form"):
        left, right = st.columns([2, 1])
        with left:
            story = st.text_area("TELL US YOUR STORY", placeholder="A rainy coffee shop... a starlit night...", height=150)
        with right:
            metal = st.selectbox("METAL", ["Polished Platinum", "18k Yellow Gold", "Champagne Gold"])
            style = st.selectbox("STYLE", ["Modernist", "Classical", "Art Nouveau"])
            forge_clicked = st.form_submit_button("FORGE MASTERPIECE")
    
    if forge_clicked and story:
        st.session_state.forged = True
        st.session_state.img_seed = len(story) + time.time()
    
    st.markdown('</div>', unsafe_allow_html=True)

# --- GENERATED SECTION ---
if st.session_state.forged:
    st.markdown("<br><br>", unsafe_allow_html=True)
    col_img, col_chat = st.columns([1, 1])
    
    with col_img:
        # Static luxury jewelry image for demo, dynamic seed for "new" feel
        st.image(f"https://picsum.photos/seed/{st.session_state.img_seed}/1000/1000", caption="DESIGN CONCEPT #001", use_container_width=True)
    
    with col_chat:
        if not st.session_state.chat_mode:
            st.markdown("### <span style='color:#b38728; font-family:Cinzel;'>The Masterpiece is Ready</span>", unsafe_allow_html=True)
            st.write("Your story has been forged into a unique design. To discuss the logistics of your proposal, speak with our AI Consultant.")
            
            if st.button("BOOK PRIVATE CONSULTATION"):
                st.session_state.chat_mode = True
                st.rerun()
        else:
            # --- AI CONCIERGE CHATBOT ---
            st.markdown("### <span style='color:#b38728; font-family:Cinzel;'>Consultation Chat</span>", unsafe_allow_html=True)
            
            # Chat Container
            st.markdown('<div class="chat-window">', unsafe_allow_html=True)
            st.markdown('<div class="bot-msg"><b>Concierge:</b> I am honored to help you plan this moment. Based on your story, should we focus on the proposal location or a custom script?</div>', unsafe_allow_html=True)
            
            # Display chat history
            for msg in st.session_state.messages:
                st.markdown(f'<div class="user-msg">{msg}</div>', unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)
            
            user_msg = st.text_input("Type your message to the concierge...")
            if st.button("SEND MESSAGE"):
                if user_msg:
                    st.session_state.messages.append(user_msg)
                    st.rerun()

            if st.button("BACK TO SPECS"):
                st.session_state.chat_mode = False
                st.rerun()
