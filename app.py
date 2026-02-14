import streamlit as st
import time
import random

# --- PAGE CONFIG ---
st.set_page_config(page_title="Avenir | High Jewelry", page_icon="✨", layout="wide")

# --- REGAL GOLD & WHITE CSS ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@400;700&family=Playfair+Display:ital,wght@0,400;1,700&family=Inter:wght@200;400&display=swap');

    /* Pure White Canvas */
    .stApp {
        background-color: #ffffff;
        color: #1a1a1a;
        font-family: 'Inter', sans-serif;
    }

    /* Avenir Gold Header */
    .avenir-logo {
        font-family: 'Cinzel', serif;
        background: linear-gradient(to bottom, #c5a059 0%, #f1d38e 50%, #b38728 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 5.5rem;
        text-align: center;
        font-weight: 700;
        letter-spacing: 15px;
        margin-top: 40px;
        margin-bottom: 0px;
        text-transform: uppercase;
    }

    .tagline {
        text-align: center;
        font-family: 'Playfair Display', serif;
        font-style: italic;
        letter-spacing: 3px;
        color: #b38728; /* Solid Gold Color */
        font-size: 0.9rem;
        margin-bottom: 50px;
    }

    /* Regal Card Styling */
    .atelier-box {
        background: #ffffff;
        border: 1px solid #f1d38e;
        padding: 60px;
        border-radius: 0px;
        box-shadow: 0 10px 50px rgba(179, 135, 40, 0.1);
        margin-bottom: 40px;
    }

    /* Gold Action Button */
    div.stButton > button {
        background: linear-gradient(45deg, #b38728 0%, #f1d38e 100%);
        color: #ffffff !important;
        border: none;
        border-radius: 0px;
        padding: 18px 45px;
        font-family: 'Cinzel', serif;
        letter-spacing: 3px;
        font-size: 0.9rem;
        font-weight: bold;
        transition: all 0.5s ease;
        width: 100%;
        margin-top: 20px;
        cursor: pointer;
    }

    div.stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 15px 30px rgba(179, 135, 40, 0.3);
        color: #ffffff !important;
    }

    /* Concierge Chatbox Styling */
    .concierge-card {
        background: #fdfaf4; /* Subtle warm cream */
        border-top: 2px solid #b38728;
        padding: 30px;
        margin-top: 20px;
        border-radius: 4px;
    }

    .concierge-title {
        font-family: 'Cinzel', serif;
        color: #b38728;
        font-size: 1rem;
        margin-bottom: 15px;
        letter-spacing: 2px;
    }

    .proposal-text {
        font-family: 'Playfair Display', serif;
        font-size: 1.3rem;
        line-height: 1.6;
        color: #333;
        font-style: italic;
    }

    /* Form Inputs */
    .stTextArea textarea {
        border: 1px solid #f1d38e !important;
        background-color: #fff !important;
    }
    </style>
    """, unsafe_allow_html=True)

# --- HEADER ---
st.markdown('<p class="avenir-logo">Avenir</p>', unsafe_allow_html=True)
st.markdown('<p class="tagline">The Art of the Heirloom</p>', unsafe_allow_html=True)

# --- THE ATELIER FORM ---
with st.container():
    st.markdown('<div class="atelier-box">', unsafe_allow_html=True)
    
    with st.form("avenir_atelier_v2"):
        col1, col2 = st.columns([1.6, 1])
        
        with col1:
            st.markdown("<p style='color:#b38728; font-family:Cinzel;'>The Narrative</p>", unsafe_allow_html=True)
            story_input = st.text_area("", placeholder="Recount the story that defines your bond...", height=170, label_visibility="collapsed")
        
        with col2:
            st.markdown("<p style='color:#b38728; font-family:Cinzel;'>The Essence</p>", unsafe_allow_html=True)
            p_style = st.selectbox("Form Factor", ["Classical Solitaire", "Art Deco Halo", "Modernist Band"])
            metal_choice = st.selectbox("Metal Finish", ["18k Yellow Gold", "Brushed Champagne Gold", "Antique Vermeil"])
            
            submit_forge = st.form_submit_button("FORGE YOUR DESIGN")
            
    st.markdown('</div>', unsafe_allow_html=True)

# --- DYNAMIC REVEAL ---
if submit_forge:
    if not story_input:
        st.error("The Atelier requires a story to begin the distillation process.")
    else:
        with st.spinner("Distilling memories into gold..."):
            time.sleep(2) # Simulated processing
            
            st.markdown("---")
            res_left, res_right = st.columns([1, 1.2])
            
            with res_left:
                # Forces a fresh image every click by using time as a seed
                unique_id = int(time.time())
                st.image(f"https://picsum.photos/seed/{unique_id}/1000/1000", 
                         caption=f"Handcrafted Design for: {p_style}", 
                         use_container_width=True)
            
            with res_right:
                st.markdown(f"### <span style='color:#b38728; font-family:Cinzel;'>The Proposal Plan</span>", unsafe_allow_html=True)
                
                # Dynamic Proposal Helper logic
                st.markdown(f"""
                <div class="concierge-card">
                    <div class="concierge-title">THE CONCIERGE'S ADVICE</div>
                    <p class="proposal-text">
                    "Your memory of {story_input[:40]}... suggests a bond of profound depth. 
                    Present this {p_style} in a setting of complete stillness—perhaps a sunrise hike or a quiet library. 
                    <br><br>
                    <strong>Your Script:</strong><br>
                    'This {metal_choice} piece was forged from the story of us. Just as this design is one-of-a-kind, 
                    my life has been uniquely transformed by you. Will you continue this story with me?'"
                    </p>
                </div>
                """, unsafe_allow_html=True)
                
                st.markdown("---")
                st.markdown("<p style='letter-spacing:2px; font-size:0.8rem; color:#888;'>CERTIFIED BY AVENIR ATELIER | 2026</p>", unsafe_allow_html=True)
                
                if st.button("BOOK A PRIVATE CONSULTATION"):
                    st.balloons()
                    st.success("Your request has been sent to our master jeweler.")
