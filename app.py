import streamlit as st
import google.generativeai as genai
from PIL import Image
import time

# 1. Page Configuration & Diamond Theme UI
st.set_page_config(page_title="Diamond AI OTC Predictor", page_icon="💎", layout="wide")

# Custom CSS for Background and Premium Look
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
        color: #f8fafc;
    }
    div.stButton > button:first-child {
        background: linear-gradient(90deg, #06b6d4 0%, #3b82f6 100%);
        color: white;
        border: none;
        padding: 15px 30px;
        font-size: 20px;
        font-weight: bold;
        border-radius: 50px;
        width: 100%;
        box-shadow: 0 4px 15px rgba(6, 182, 212, 0.4);
        transition: 0.3s;
    }
    div.stButton > button:hover {
        transform: scale(1.02);
        box-shadow: 0 6px 20px rgba(6, 182, 212, 0.6);
    }
    .result-card {
        background-color: rgba(30, 41, 59, 0.7);
        padding: 25px;
        border-radius: 15px;
        border: 1px solid #334155;
        margin-top: 20px;
    }
    .status-bar {
        border-radius: 10px;
        padding: 10px;
        text-align: center;
        font-weight: bold;
    }
    </style>
""", unsafe_allowed_html=True)

# 2. Integrate Your API Key
API_KEY = "AQ.Ab8RN6Idmj_Y2q2q4u7ryWAYRr2uIyZALe0Qqe9CdfjgJiAxNw"
genai.configure(api_key=API_KEY)

# Header Section
st.markdown("<h1 style='text-align: center; color: #22d3ee;'>💎 DIAMOND AI OTC ANALYZER v2.0</h1>", unsafe_allowed_html=True)
st.markdown("<p style='text-align: center; color: #94a3b8;'>Advanced Candlestick Analysis with Neural Network Technology</p>", unsafe_allowed_html=True)

# 3. Sidebar Configuration (Professional Inputs)
st.sidebar.image("https://cdn-icons-png.flaticon.com/512/3665/3665923.png", width=80)
st.sidebar.title("Configuration")
market_type = st.sidebar.selectbox("Market Type", ["Quotex OTC Market", "Pocket Option OTC", "Binary.com OTC", "Live Forex Market"])
currency_pair = st.sidebar.text_input("Asset Name", "USD/JPY (OTC)")
timeframe = st.sidebar.selectbox("Analysis Timeframe", ["1 Minute", "2 Minutes", "5 Minutes", "15 Minutes"])

# 4. Main Interface
col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("📁 Upload Trading Chart")
    uploaded_file = st.file_uploader("Drop your screenshot here...", type=["jpg", "jpeg", "png"])
    if uploaded_file:
        image = Image.open(uploaded_file)
        st.image(image, caption="Current Chart Pattern", use_container_width=True)

with col2:
    st.subheader("⚡ AI Processing Hub")
    if uploaded_file is not None:
        if st.button("ANALYZE NOW"):
            progress_bar = st.progress(0)
            status_text = st.empty()
            
            # Simulated Loading Animation
            for percent_complete in range(100):
                time.sleep(0.01)
                progress_bar.progress(percent_complete + 1)
                status_text.text(f"Scanning Candlestick Volatility... {percent_complete}%")
            
            try:
                # Optimized Professional Prompt
                prompt = f"""
                Act as a Professional Financial Master Trader with 15 years of experience in OTC Binary Options. 
                Analyze this chart for {currency_pair} on {market_type} with a {timeframe} candle period.
                Your response must be in strictly ENGLISH and very detailed.
                Use the following format for results:
                
                NEXT SIGNAL: [CALL / PUT / NEUTRAL]
                SIGNAL ACCURACY: [Mention specific %, e.g., 92%]
                
                TECHNICAL METRICS:
                - Market Trend: (Explain the current trend)
                - Candle Pattern Found: (Mention patterns like Hammer, Doji, Marubozu etc)
                - Resistance & Support: (Give specific price levels from the chart)
                - Momentum Score: (Out of 100)
                
                TRADING ADVICE:
                (Give a professional expert tip for this trade)
                """
                
                model = genai.GenerativeModel('gemini-1.5-flash')
                response = model.generate_content([prompt, image])
                
                status_text.markdown("<div class='status-bar' style='background-color: #064e3b; color: #34d399;'>Analysis Successful!</div>", unsafe_allowed_html=True)
                
                # Display Results in Diamond Style
                st.markdown("<div class='result-card'>", unsafe_allowed_html=True)
                st.subheader("🎯 Prediction Output")
                st.write(response.text)
                st.markdown("</div>", unsafe_allowed_html=True)
                
            except Exception as e:
                st.error(f"System Error: {str(e)}")
    else:
        st.warning("Please upload a chart screenshot to initiate the AI scanner.")

# Footer
st.markdown("---")
st.markdown("<p style='text-align: center; color: #475569;'>Powered by Gemini AI - Professional Trading Systems</p>", unsafe_allowed_html=True)
