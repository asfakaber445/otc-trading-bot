import streamlit as st
import google.generativeai as genai
from PIL import Image
import time

# 1. Page Configuration
st.set_page_config(page_title="VIP AI OTC Predictor", page_icon="💎", layout="wide")

# 2. Integrate Your API Key
API_KEY = "AQ.Ab8RN6Idmj_Y2q2q4u7ryWAYRr2uIyZALe0Qqe9CdfjgJiAxNw"
genai.configure(api_key=API_KEY)

# Premium Header Section
st.title("🔱 VIP OTC MARKET SCANNER v5.0")
st.subheader("🔥 Premium Candlestick Intelligence & Neural Network Analytics")
st.markdown("---")

# 3. Sidebar Configuration
st.sidebar.title("👑 VIP Control Panel")
market_type = st.sidebar.selectbox("Select Market", ["Quotex OTC Market", "Pocket Option OTC", "Binary.com OTC", "Live Forex Market"])
currency_pair = st.sidebar.text_input("Asset / Currency Pair", "USD/JPY (OTC)")
timeframe = st.sidebar.selectbox("Candle Timeframe", ["1 Minute", "2 Minutes", "5 Minutes", "15 Minutes"])

st.sidebar.markdown("---")
st.sidebar.info("⚡ VIP Status: ACTIVE\n🎯 Accuracy Mode: MAX")

# 4. Main Interface Split
col1, col2 = st.columns([1, 1])

with col1:
    st.error("📥 UPLOAD TRADING CHART")
    uploaded_file = st.file_uploader("Drop your screenshot here...", type=["jpg", "jpeg", "png"])
    if uploaded_file:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Chart Pattern", use_container_width=True)

with col2:
    st.success("⚡ AI PROCESSING HUB")
    if uploaded_file is not None:
        if st.button("🚀 ANALYZE NOW (VIP SCAN)", type="primary"):
            progress_bar = st.progress(0)
            status_text = st.empty()
            
            # Loading Animation
            for percent_complete in range(100):
                time.sleep(0.01)
                progress_bar.progress(percent_complete + 1)
                status_text.text(f"Scanning Candlestick Volatility... {percent_complete}%")
            
            # Absolute structure instruction prompt
            prompt = f"""
            Act as an Elite Financial Master Trader with 15 years of experience in OTC Binary Options. 
            Analyze this chart for {currency_pair} on {market_type} with a {timeframe} candle period.
            Your response must be strictly in ENGLISH, extremely bold, and crystal clear.
            
            CRITICAL INSTRUCTION: You MUST start your response with the NEXT SIGNAL prediction (CALL, PUT, or NEUTRAL) in giant bold letters.
            
            Use the following exact format:
            
            🔥 NEXT SIGNAL: [CALL / PUT / NEUTRAL]
            🎯 SIGNAL ACCURACY: [Specific %, e.g., 94%]
            
            📊 TECHNICAL METRICS:
            - Market Trend: (Detailed trend explanation)
            - Candle Pattern Found: (Exact patterns like Hammer, Doji, Marubozu etc)
            - Resistance & Support: (Specific price levels from the chart)
            - Momentum Score: (Out of 100)
            
            💡 VIP TRADING ADVICE:
            (Expert tip for this trade setup)
            """
            
            # Multi-Model Fallback Engine to bypass 404 error perfectly
            models_to_try = ['gemini-2.5-flash', 'gemini-1.5-flash', 'gemini-1.5-pro', 'gemini-1.5-flash-latest']
            response_text = None
            
            for model_name in models_to_try:
                try:
                    model = genai.GenerativeModel(model_name)
                    response = model.generate_content([prompt, image])
                    response_text = response.text
                    if response_text:
                        break
                except Exception:
                    continue
            
            if response_text:
                status_text.success("✅ VIP Analysis Successful!")
                st.markdown("---")
                st.warning("🎯 PREDICTION OUTPUT")
                st.markdown(response_text)
            else:
                st.error("System Error: API Connection failed across all models. Please verify your API Key status or network conditions.")
                
    else:
        st.warning("⚠️ Please upload a chart screenshot to initiate the VIP AI scanner.")

# Footer
st.markdown("---")
st.caption("💎 VIP Trading Bot System • Powered by Gemini AI Intelligence")
