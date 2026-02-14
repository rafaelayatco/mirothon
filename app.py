import streamlit as st
import time

# --- CONFIG ---
st.set_page_config(page_title="Avenir | High Jewelry", page_icon="✨", layout="wide")

# --- INITIALIZING SESSION STATE ---
# This ensures the image and chat stay active when the user interacts
if 'forged' not in st.session_state:
    st.session_state.forged = False
if 'chat_mode' not in st.session_state:
    st.session_state.chat_mode = False
if 'image_url' not in st.session_state:
    st.session_state.image_url = ""

# --- REGAL GOLD & WHITE CSS ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@400;700&family=Playfair+Display:ital,wght@0,400;1,700&family=Inter:wght@200;400&display=swap');

    .stApp { background-color: #ffffff; color: #1a1a1a; font-family: 'Inter', sans-serif; }

    /* Hero Banner Picture */
    .hero-banner {
        width: 100%;
        height: 300px;
        background-image: url('https://images.unsplash.com/photo-1515377905703-c4788e51af15?q=80&w=2000');
        background-size: cover;
        background-position: center;
        display: flex;
        align-items: center;
        justify-content: center;
        margin-bottom: 50px;
        border-bottom: 3px solid #b38728;
    }

    .avenir-logo {
        font-family: 'Cinzel', serif;
        color: #ffffff;
        background: linear-gradient(to bottom, #c5a059 0%, #f1d38e 50%, #b38728 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 6rem;
        font-weight: 700;
        letter-spacing: 20px;
        text-transform: uppercase;
        filter: drop-shadow(0 5px 15px rgba(0,0,0,0.3));
    }

    /* Input Section */
    .atelier-input-container {
        background: #fdfaf4;
        padding: 40px;
        border: 1px solid #f1d38e;
        margin-top: -80px; /* Overlap effect */
        position: relative;
        z-index: 10;
        box-shadow: 0 20px 40px rgba(0,0,0,0.05);
    }

    /* Buttons */
    div.stButton > button {
        background: linear-gradient(45deg, #b38728 0%, #f1d38e 100%);
        color: #ffffff !important;
        border: none;
        border-radius: 0px;
        padding: 15px 45px;
        font-family: 'Cinzel', serif;
        letter-spacing: 3px;
        font-weight: bold;
        width: 100%;
        transition: 0.4s;
    }

    /* Chat Bubbles */
    .chat-container {
        background: #f9f9f9;
        padding: 20px;
        border: 1px solid #eee;
        height: 300px;
        overflow-y: auto;
        margin-bottom: 10px;
        font-family: 'Playfair Display', serif;
    }
    
    .stTextArea textarea { border: 1px solid #f1d38e !important; }
    </style>
    """, unsafe_allow_html=True)

# --- HERO BANNER ---
st.markdown('<div class="hero-banner"><p class="avenir-logo">Avenir</p></div>', unsafe_allow_html=True)

# --- INPUT AREA ---
with st.container():
    st.markdown('<div class="atelier-input-container">', unsafe_allow_html=True)
    col_input, col_opt = st.columns([2, 1])
    
    with col_input:
        story_text = st.text_area("THE NARRATIVE", placeholder="Share your story...", height=150)
    with col_opt:
        metal = st.selectbox("Metal Selection", ["Satin White Gold", "18k Champagne Gold", "Polished Platinum"])
        if st.button("FORGE PIECE"):
            if story_text:
                st.session_state.forged = True
                # Generating a unique high-res image link (Simulating DALL-E)
                st.session_state.image_url = f"https://picsum.photos/seed/{len(story_text) + time.time()}/1000/1000"
    st.markdown('</div>', unsafe_allow_html=True)

# --- DYNAMIC RESULTS ---
if st.session_state.forged:
    st.markdown("---")
    res_left, res_right = st.columns([1, 1])
    
    with res_left:
        st.image(st.session_state.image_url, caption="PROTOTYPE DESIGN", use_container_width=True)
    
    with res_right:
        if not st.session_state.chat_mode:
            st.markdown("### <span style='color:#b38728; font-family:Cinzel;'>The Reveal</span>", unsafe_allow_html=True)
            st.write("Your design has been calculated. The next step is the moment of presentation.")
            if st.button("BOOK PRIVATE CONSULTATION"):
                st.session_state.chat_mode = True
                st.rerun()
        else:
            # --- AI CHATBOT INTERFACE ---
            st.markdown("### <span style='color:#b38728; font-family:Cinzel;'>Concierge Chat</span>", unsafe_allow_html=True)
            st.markdown('<div class="chat-container"><i>Avenir Concierge:</i> "I am here to help you plan the perfect proposal. Based on your story, would you like to discuss the location or the words you will say?"</div>', unsafe_allow_html=True)
            
            chat_input = st.text_input("Speak with your consultant...")
            if chat_input:
                st.toast("Processing your request...", icon="✨")
                # Here you would typically append the user message to a list in session_state
            
            if st.button("← BACK TO SPECS"):
                st.session_state.chat_mode = False
                st.rerun()
