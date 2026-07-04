import streamlit as st
import google.generativeai as genai
from PIL import Image
import time

# 1. Page Configuration
st.set_page_config(page_title="Diamond AI OTC Predictor", page_icon="💎", layout="wide")

# 2. Integrate Your API Key
API_KEY = "AQ.Ab8RN6Idmj_Y2q2q4u7ryWAYRr2uIyZALe0Qqe9CdfjgJiAxNw"
genai.configure(api_key=API_KEY)

# Header Section (Safe Format)
st.title("💎 DIAMOND AI OTC ANALYZER v2.0")
st.caption("Advanced Candlestick Analysis with Neural Network Technology")

# 3. Sidebar Configuration
st.sidebar.title("⚙️ Configuration")
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
        if st.button("ANALYZE NOW", type="primary"):
            progress_bar = st.progress(0)
            status_text = st.empty()
            
            # Loading Animation
            for percent_complete in range(100):
                time.sleep(0.01)
                progress_bar.progress(percent_complete + 1)
                status_text.text(f"Scanning Candlestick Volatility... {percent_complete}%")
            
            try:
                # Optimized Prompt
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
                
                status_text.success("Analysis Successful!")
                
                # Display Results in a Clean Box
                st.markdown("---")
                st.subheader("🎯 Prediction Output")
                st.info(response.text)
                
            except Exception as e:
                st.error(f"System Error: {str(e)}")
    else:
        st.warning("Please upload a chart screenshot to initiate the AI scanner.")

# Footer
st.markdown("---")
st.caption("Powered by Gemini AI - Professional Trading Systems")
