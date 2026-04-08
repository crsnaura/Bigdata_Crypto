import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# =========================
# CONFIG
# =========================
st.set_page_config(page_title="🚀 Crypto Terminal Pro", layout="wide")

# =========================
# CSS (SOFT NEON - EYE FRIENDLY)
# =========================
st.markdown("""
<style>
/* Background utama tetap gelap tapi lebih soft */
.stApp {
    background-color: #0d1117;
}

/* JUDUL UTAMA (H1) - Glow diperhalus */
h1 {
    color: #ffffff !important;
    text-align: center;
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    /* Bayangan tipis saja supaya tidak silau */
    text-shadow: 2px 2px 8px rgba(0, 212, 255, 0.5);
    padding: 20px;
}

/* SUB-JUDUL & LABEL */
h2, h3, label {
    color: #b0fbff !important; /* Biru sangat muda, hampir putih */
    text-shadow: 1px 1px 3px rgba(0, 212, 255, 0.3);
}

/* SIDEBAR - Hilangkan pendaran berlebih */
section[data-testid="stSidebar"] {
    background-color: #0a0d12 !important;
    border-right: 1px solid #1f2937;
}

/* Teks di Sidebar dibuat putih bersih */
section[data-testid="stSidebar"] * {
    color: #e0e0e0 !important;
}

/* Judul di Sidebar dikasih aksen biru tipis di bawahnya saja */
section[data-testid="stSidebar"] h1 {
    font-size: 1.5rem !important;
    border-bottom: 2px solid #00d4ff;
    padding-bottom: 10px;
    text-shadow: none !important;
}

/* METRIC - Angka putih tajam tanpa bayangan kabur */
[data-testid="stMetricValue"] {
    color: #ffffff !important;
    font-weight: bold !important;
}

/* INPUT BOX - Border biru gelap saja */
.stTextInput input, .stSelectbox div[data-baseweb="select"] {
    background-color: #161b22 !important;
    color: #ffffff !important;
    border: 1px solid #30363d !important;
}

/* Hover effect biar tetep interaktif tapi gak silau */
.stTextInput input:focus {
    border-color: #58a6ff !important;
    box-shadow: 0 0 5px rgba(88, 166, 255, 0.2);
}
</style>
""", unsafe_allow_html=True)

# =========================
# LOAD DATA
# =========================
# Asumsi path tetap sama
try:
    df = pd.read_csv("data/clean_crypto_data.csv")
    df["date"] = pd.to_datetime(df["date"])
except:
    st.error("Data tidak ditemukan! Pastikan file CSV ada di folder 'data/'.")
    st.stop()

# =========================
# SIDEBAR
# =========================
st.sidebar.title("⚡ TERMINAL MENU")

menu = st.sidebar.selectbox("Navigation", [
    "📊 Market Overview",
    "🔍 AI Smart Search",
    "🔮 Trend Analysis",
    "💰 Portfolio Simulator" # <--- FITUR BARU!
])

coin = st.sidebar.selectbox(
    "💎 Select Asset",
    df["coin"].unique()
)

subset = df[df["coin"] == coin].sort_values("date")

st.sidebar.markdown("---")
st.sidebar.info("Update: Real-time Analysis Active")

# =========================
# HEADER
# =========================
st.title("🚀 Crypto Market Intelligence")
st.markdown(f"Active Monitoring: **{coin} / USDT**")

# =========================
# 1. MARKET OVERVIEW
# =========================
if "Market Overview" in menu:
    st.subheader("📊 Key Metrics")
    
    col1, col2, col3, col4 = st.columns(4)
    
    last_price = subset['price'].iloc[-1]
    prev_price = subset['price'].iloc[-2]
    delta_price = ((last_price - prev_price) / prev_price) * 100

    col1.metric("Current Price", f"${last_price:,.2f}", f"{delta_price:.2f}%")
    col2.metric("7d Volatility", f"{subset['volatility_7d'].iloc[-1]:.4f}")
    col3.metric("Daily Return", f"{subset['return'].iloc[-1]:.4f}")
    col4.metric("Market Status", "🟢 Bullish" if subset["ma_7"].iloc[-1] > subset["ma_30"].iloc[-1] else "🔴 Bearish")

    st.markdown("---")
    st.subheader("📈 Price Movement")
    
    fig, ax = plt.subplots(figsize=(10, 4))
    ax.set_facecolor('#0e1117')
    fig.patch.set_facecolor('#0e1117')
    
    ax.plot(subset["date"], subset["price"], color='#00d4ff', linewidth=2)
    ax.fill_between(subset["date"], subset["price"], color='#00d4ff', alpha=0.1)
    
    ax.tick_params(axis='x', colors='white')
    ax.tick_params(axis='y', colors='white')
    ax.spines['bottom'].set_color('white')
    ax.spines['left'].set_color('white')
    
    st.pyplot(fig)

# =========================
# 2. AI SMART SEARCH
# =========================
elif "AI Smart Search" in menu:
    st.subheader("🔍 Query Assistant")
    
    search = st.text_input("Ask about market trends...", placeholder="e.g. price, volatility, trend")

    if search:
        st.write("---")
        if "price" in search.lower() or "harga" in search.lower():
            st.success(f"**Live Report:** The current price of {coin} is **${subset['price'].iloc[-1]:,.2f}**")
        elif "volatility" in search.lower() or "volatilitas" in search.lower():
            st.warning(f"**Risk Alert:** {coin} shows a volatility level of **{subset['volatility_7d'].iloc[-1]:.4f}**")
        else:
            st.info("💡 Try asking about 'price' or 'trend'.")

# =========================
# 3. TREND ANALYSIS
# =========================
elif "Trend Analysis" in menu:
    st.subheader("🔮 Predictive Signals")
    
    ma7 = subset["ma_7"].iloc[-1]
    ma30 = subset["ma_30"].iloc[-1]
    
    if ma7 > ma30:
        st.markdown("""<div style='background-color: #064e3b; padding: 20px; border-radius: 10px;'>
                    <h3 style='color: #10b981;'>🚀 BULLISH SIGNAL DETECTED</h3>
                    <p style='color: white;'>Short-term momentum is stronger than long-term average.</p>
                    </div>""", unsafe_allow_html=True)
    else:
        st.markdown("""<div style='background-color: #7f1d1d; padding: 20px; border-radius: 10px;'>
                    <h3 style='color: #ef4444;'>⚠️ BEARISH CAUTION</h3>
                    <p style='color: white;'>The market is currently under pressure. Stay cautious.</p>
                    </div>""", unsafe_allow_html=True)

    fig, ax = plt.subplots(figsize=(10, 4))
    fig.patch.set_facecolor('#0e1117')
    ax.set_facecolor('#0e1117')
    
    ax.plot(subset["date"], subset["price"], label="Price", color='gray', alpha=0.5)
    ax.plot(subset["date"], subset["ma_7"], label="Fast (MA 7)", color='#00d4ff')
    ax.plot(subset["date"], subset["ma_30"], label="Slow (MA 30)", color='#ff007c')
    
    ax.legend()
    st.pyplot(fig)

# =========================
# 4. PORTFOLIO SIMULATOR (BARU)
# =========================
elif "Portfolio Simulator" in menu:
    st.subheader("💰 Investment Simulator")
    st.write("Cek berapa cuanmu kalau seandainya beli koin ini beberapa hari lalu!")
    
    investment = st.number_input("Modal Investasi ($)", min_value=10, value=100)
    days_ago = st.slider("Beli berapa hari yang lalu?", 1, 30, 7)
    
    price_then = subset['price'].iloc[-days_ago]
    price_now = subset['price'].iloc[-1]
    
    total_coins = investment / price_then
    current_value = total_coins * price_now
    profit = current_value - investment
    percent = (profit / investment) * 100
    
    st.markdown("---")
    c1, c2 = st.columns(2)
    with c1:
        st.write(f"Harga saat beli: **${price_then:,.2f}**")
        st.write(f"Harga sekarang: **${price_now:,.2f}**")
    with c2:
        if profit >= 0:
            st.metric("Estimasi Profit", f"${profit:,.2f}", f"+{percent:.2f}%")
        else:
            st.metric("Estimasi Rugi", f"${profit:,.2f}", f"{percent:.2f}%")