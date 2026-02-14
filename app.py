import streamlit as st
import time
import random

# --- PAGE CONFIG ---
st.set_page_config(page_title="The Generative Jeweler", page_icon="💍", layout="wide")

# --- WHITE GOLD & MARBLE CSS ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@300;600&family=Montserrat:wght@200;400&display=swap');

    /* Background: Silk/Marble feel */
    .stApp {
        background: linear-gradient(135deg, #fdfbfb 0%, #ebedee 100%);
        color: #2c3e50;
        font-family: 'Montserrat', sans-serif;
    }

    /* White Gold Header */
    .white-gold-header {
        font-family: 'Cormorant Garamond', serif;
        background: linear-gradient(90deg, #d1d1d1 0%, #ffffff 50%, #d1d1d1 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        filter: drop-shadow(0px 2px 2px rgba(0,0,0,0.1));
        font-size: 4.5rem;
        text-align: center;
        font-weight: 600;
        margin-bottom: 10px;
    }

    /* Luxury Boutique Card */
    .boutique-card {
        background: rgba(255, 255, 255, 0.7);
        border: 1px solid rgba(200, 200, 200, 0.4);
        padding: 40px;
        border-radius: 15px;
        box-shadow: 0 15px 35px rgba(0,0,0,0.05);
        backdrop-filter: blur(10px);
        margin-bottom: 30px;
    }

    /* Platinum Button */
    div.stButton > button {
        background: linear-gradient(145deg, #ffffff, #e6e6e6);
        color: #444 !important;
        border: 1px solid #ccc;
        border-radius: 0px;
        padding: 12px 30px;
        font-family: 'Montserrat', sans-serif;
        letter-spacing: 3px;
        text-transform: uppercase;
        transition: 0.3s;
        width: 100%;
    }

    div.stButton > button:hover {
        background: #f8f8f8;
        border: 1px solid #888;
        box-shadow: 0 5px 15px rgba(0,0,0,0.1);
        color: #000 !important;
    }

    /* Typography */
    h3 {
        font-family: 'Cormorant Garamond', serif !important;
        color: #555 !important;
        border-bottom: 1px solid #ddd;
        padding-bottom: 10px;
    }
    
    .stTextArea textarea { border-radius: 0px !important; border: 1px solid #ddd !important; }
    </style>
    """, unsafe_allow_html=True)

# --- APP CONTENT ---
st.markdown('<h1 class="white-gold-header">The Atelier</h1>', unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color: #888; letter-spacing: 5px; text-transform: uppercase; font-size: 0.8rem;'>Bespoke Generative Jewelry</p>", unsafe_allow_html=True)

# Use a form to ensure that clicking the button clears/refreshes the state properly
with st.container():
    st.markdown('<div class="boutique-card">', unsafe_allow_html=True)
    with st.form("jewelry_form", clear_on_submit=False):
        col1, col2 = st.columns([2, 1])
        
        with col1:
            user_story = st.text_area("SHARE YOUR STORY", placeholder="Describe the moment you want to freeze in precious metal...", height=150)
        
        with col2:
            piece_type = st.selectbox("CATEGORY", ["Engagement Ring", "Memory Pendant", "Sculptural Cuff"])
            finish = st.selectbox("FINISH", ["High-Polish White Gold", "Satin Platinum", "Brushed Silver"])
            submitted = st.form_submit_button("COMMISSION DESIGN")
    st.markdown('</div>', unsafe_allow_html=True)

# --- REGENERATION LOGIC ---
if submitted:
    if not user_story:
        st.error("Please whisper your story to the Atelier first.")
    else:
        # Create a "unique" seed based on the story to force a fresh feeling
        random_seed = random.randint(1, 10000)
        
        with st.spinner("Refining geometry and setting stones..."):
            # Simulate the generation delay
            time.sleep(2)
            
            st.markdown("---")
            res_col1, res_col2 = st.columns([1, 1])
            
            with res_col1:
                st.markdown("### The Visual Concept")
                # Using a dynamic placeholder that changes with the story length to simulate different results
                # In production, replace this with your DALL-E 3 image URL logic
                image_id = (len(user_story) % 5) + 1 
                st.image(f"https://picsum.photos/seed/{random_seed}/800/800", caption="Generated Prototype V1.0", use_container_width=True)
                
            with res_col2:
                st.markdown("### Design Specs")
                st.write(f"**Material:** {finish}")
                st.write(f"**Collection:** *The {piece_type} Series*")
                
                # Logic to "extract" concepts (Simulated)
                st.success("✅ Generative 3D Mesh Ready")
                st.info(f"Design analysis: Your story of '{user_story[:30]}...' has been translated into a fluid, organic lattice structure.")
                
                st.download_button(
                    label="EXPORT .OBJ FOR FABRICATION",
                    data=f"OBJ Data for {user_story}",
                    file_name="atelier_design.obj",
                    mime="text/plain"
                )
