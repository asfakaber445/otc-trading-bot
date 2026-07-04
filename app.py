import streamlit as st
import google.generativeai as genai
from PIL import Image

# ১. ড্যাশবোর্ড ও পেজ কনফিগারেশন
st.set_page_config(page_title="Quotex OTC AI Predictor", page_icon="📊", layout="centered")

st.markdown("""
    <div style="background-color:#1e293b; padding:20px; border-radius:10px; text-align:center; margin-bottom:25px;">
        <h1 style="color:#38bdf8; margin:0; font-size:28px;">📊 OTC MARKET SCANNER v1.0</h1>
        <p style="color:#94a3b8; margin:5px 0 0 0;">AI-Powered Candlestick Analytics</p>
    </div>
""", unsafe_allowed_html=True)

# ২. ফ্রি Gemini API Key বসানোর জায়গা
# (আপাতত এটি এভাবেই থাকবে, পরে আমরা আসল কি বসাবো)
API_KEY = "YOUR_GEMINI_API_KEY_HERE"
genai.configure(api_key=API_KEY)

# ৩. কন্ট্রোল প্যানেল
st.sidebar.header("⚙️ কন্ট্রোল প্যানেল")
market_type = st.sidebar.selectbox("মার্কেট টাইপ:", ["Quotex OTC Market", "Pocket Option OTC", "Live Crypto Market"])
currency_pair = st.sidebar.text_input("কারেন্সি পেয়ার:", "USD/BDT OTC")
timeframe = st.sidebar.selectbox("টাইমফ্রেম:", ["1 Min", "2 Min", "5 Min"])

# ৪. মূল ইন্টারফেস
st.subheader("📸 চার্ট আপলোড সেকশন")
uploaded_file = st.file_uploader("আপনার ওটিসি চার্টের স্ক্রিনশট এখানে আপলোড করুন...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='স্ক্যান করার জন্য প্রস্তুত চার্ট', use_container_width=True)
    
    if st.button("🔮 এআই অ্যানালাইসিস শুরু করুন", type="primary"):
        with st.spinner("এআই ওটিসি অ্যালগরিদম স্ক্যান করছে..."):
            try:
                prompt = f"""
                You are an elite binary options trader holding a 90% win rate in OTC markets.
                Strictly analyze this candlestick chart for {currency_pair} on {market_type} with a {timeframe} timeframe.
                Provide your analysis in Bengali inside clean markdown boxes with this exact structure:
                ### 🚨 পরের ক্যান্ডেল প্রেডিকশন: [CALL (UP) / PUT (DOWN) / AVOID]
                ### 📈 সম্ভাব্য উইন রেশিও (Confidence %): [যেমন: ৮২%]
                ### 🔍 টেকনিক্যাল অ্যানালাইসিস:
                - **মার্কেট ট্রেন্ড:** (Upward/Downward/Sideways)
                - **ক্যান্ডেলস্টিক প্যাটার্ন:** (যা দেখতে পাচ্ছেন)
                - **সাপোর্ট/রেজিস্ট্যান্স:** (প্রাইস লেভেল)
                ### 💡 সেফ ট্রেডিং টিপস:
                - (পরামর্শ)
                """
                
                model = genai.GenerativeModel('gemini-1.5-flash')
                response = model.generate_content([prompt, image])
                
                st.success("স্ক্যানিং সম্পন্ন হয়েছে!")
                st.markdown("---")
                st.subheader("🔮 এআই প্রেডিকশন রেজাল্ট")
                st.markdown(f"<div style='background-color:#0f172a; padding:15px; border-radius:8px; border-left:5px solid #38bdf8;'>{response.text}</div>", unsafe_allowed_html=True)
            
            except Exception as e:
                st.error(f"ভুল হয়েছে: {e}")
else:
    st.info("💡 নির্দেশিকা: আপনার ট্রেডিং প্ল্যাটফর্ম থেকে স্ক্রিনশট নিয়ে এখানে আপলোড করুন।")
