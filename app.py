import streamlit as st
import time
import random

# --- PAGE CONFIG ---
st.set_page_config(page_title="Avenir | Generative High Jewelry", page_icon="✨", layout="wide")

# --- LUXURY WHITE GOLD & MARBLE CSS ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,600;1,400&family=Inter:wght@200;400&display=swap');

    /* Silk and Soft Stone Background */
    .stApp {
        background: linear-gradient(135deg, #f5f7f7 0%, #ffffff 100%);
        color: #1a1a1a;
        font-family: 'Inter', sans-serif;
    }

    /* Avenir Branding - White Gold Gradient */
    .avenir-logo {
        font-family: 'Cormorant Garamond', serif;
        background: linear-gradient(to right, #b8b8b8 0%, #e8e8e8 50%, #b8b8b8 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 5rem;
        text-align: center;
        font-weight: 300;
        letter-spacing: 12px;
        margin-top: 50px;
        margin-bottom: 0px;
        text-transform: uppercase;
    }

    /* Subtext styling */
    .tagline {
        text-align: center;
        font-family: 'Inter', sans-serif;
        letter-spacing: 6px;
        color: #999;
        font-size: 0.7rem;
        text-transform: uppercase;
        margin-bottom: 50px;
    }

    /* Glassmorphism Container */
    .atelier-box {
        background: rgba(255, 255, 255, 0.8);
        border: 1px solid rgba(220, 220, 220, 0.5);
        padding: 50px;
        border-radius: 2px; /* Sharp architectural corners */
        box-shadow: 0 30px 60px rgba(0,0,0,0.03);
        margin-bottom: 40px;
    }

    /* The 'Platinum' Action Button */
    div.stButton > button {
        background: #1a1a1a;
        color: #ffffff !important;
        border: none;
        border-radius: 0px;
        padding: 15px 40px;
        font-family: 'Inter', sans-serif;
        letter-spacing: 4px;
        font-size: 0.8rem;
        transition: 0.4s ease;
        width: 100%;
        margin-top: 20px;
    }

    div.stButton > button:hover {
        background: #444;
        color: #ffffff !important;
        box-shadow: 0 10px 20px rgba(0,0,0,0.1);
    }

    /* Concierge Chatbox Styling */
    .chat-bubble {
        background: #ffffff;
        border-left: 3px solid #d1d1d1;
        padding: 20px;
        margin: 10px 0;
        font-style: italic;
        color: #444;
        font-family: 'Cormorant Garamond', serif;
        font-size: 1.2rem;
    }

    /* Input focus colors */
    input, textarea {
        border-radius: 0px !important;
        border-color: #eee !important;
    }
    </style>
    """, unsafe_allow_html=True)

# --- HEADER ---
st.markdown('<p class="avenir-logo">Avenir</p>', unsafe_allow_html=True)
st.markdown('<p class="tagline">High Jewelry & Narrative Design</p>', unsafe_allow_html=True)

# --- ATELIER INTERFACE ---
with st.container():
    st.markdown('<div class="atelier-box">', unsafe_allow_html=True)
    
    with st.form("avenir_form"):
        col1, col2 = st.columns([1.5, 1])
        
        with col1:
            st.markdown("##### THE NARRATIVE")
            story = st.text_area("", placeholder="Where did your hearts first align?", height=165, label_visibility="collapsed")
        
        with col2:
            st.markdown("##### PREFERENCE")
            p_type = st.selectbox("Form", ["Solitaire Ring", "Halo Pendant", "Structural Cuff"])
            metal = st.selectbox("Metal", ["Satin White Gold", "Polished Platinum", "Iridium Silver"])
            submit = st.form_submit_button("BEGIN FORGING")
            
    st.markdown('</div>', unsafe_allow_html=True)

# --- REVEAL LOGIC ---
if submit:
    if not story:
        st.error("Please share a story for the Avenir engine to interpret.")
    else:
        # Luxury Reveal Sequence
        with st.spinner("Refining your legacy..."):
            time.sleep(2.5)
            
            st.markdown("---")
            res_left, res_right = st.columns([1.2, 1])
            
            with res_left:
                # Dynamic Image Placeholder (In production, connect DALL-E 3 here)
                # We use a random seed to ensure the image changes every time they click "Forge"
                random_id = random.randint(1, 1000)
                st.image(f"https://picsum.photos/seed/{random_id}/1000/1000", caption="AVENIR PROTOTYPE V1", use_container_width=True)
            
            with res_right:
                st.markdown("### The Concierge")
                st.write("Based on your story, I have crafted a proposal plan to match the elegance of this piece:")
                
                # Mock AI Concierge Response
                st.markdown(f"""
                <div class="chat-bubble">
                "Since your story began in {story[:20]}..., I suggest a quiet evening. 
                Wait until the blue hour. Present this {p_type} not as a gift, 
                but as a physical anchor to that first rainy afternoon. 
                Say this: 'I wanted to give you something that finally matches 
                the weight of my memory of us.'"
                </div>
                """, unsafe_allow_html=True)
                
                st.markdown("---")
                st.markdown("##### MATERIAL SUMMARY")
                st.write(f"• **Alloy:** {metal}")
                st.write(f"• **Concept:** Organic Sentimentality")
                st.write(f"• **Reference:** #AV-{random_id}")
                
                if st.button("SEND TO CONSULTANT"):
                    st.toast("A private concierge will contact you shortly.", icon="✨")
