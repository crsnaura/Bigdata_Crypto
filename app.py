import streamlit as st
import pandas as pd
import time
import seaborn as sns
import matplotlib.pyplot as plt
import requests

st.set_page_config(page_title="🚀 Crypto Dashboard", layout="wide")

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
df_price = pd.read_csv("hourly_price.csv")
df_cum = pd.read_csv("cum_return.csv")
df_log = pd.read_csv("log_return.csv")

df_price["timestamp"] = pd.to_datetime(df_price["timestamp"])
df_cum["timestamp"] = pd.to_datetime(df_cum["timestamp"])
df_log["timestamp"] = pd.to_datetime(df_log["timestamp"])

# =========================
# SIDEBAR
# =========================
st.sidebar.title("⚡ TERMINAL MENU")

menu = st.sidebar.selectbox("Navigation", [
    "📊 Market Overview",
    "📈 Performance",
    "🔥 Correlation",
    "🧠 Insights",
    "🔮 Trend Analysis",
    "💰 Portfolio Simulator" 
])

coin = st.sidebar.selectbox(
    "💎 Select Asset",
    df_price.columns[1:]
)

st.sidebar.markdown("---")
st.sidebar.info("Update: Real-time Analysis Active")

# =========================
# HEADER
# =========================
st.title("🚀 Crypto Market Intelligence")
st.markdown(f"Active Monitoring: **{coin} / USDT**")

# =========================
# SUBSET DATA
# =========================
subset_price = df_price[["timestamp", coin]].dropna()
subset_cum = df_cum[["timestamp", coin]].dropna()

# =========================
# MARKET OVERVIEW
# =========================
st.markdown("## 💡 What is Cryptocurrency?")

st.markdown("""
<div style='text-align:justify; font-size:22px; line-height:1.8; color:#e2e8f0;'>

Cryptocurrency adalah aset digital berbasis teknologi blockchain yang tidak dikontrol oleh pihak pusat seperti bank atau pemerintah. 
Sistem ini memungkinkan transaksi dilakukan secara langsung antar pengguna dengan tingkat transparansi dan keamanan yang tinggi. Dalam dunia modern, cryptocurrency tidak hanya digunakan sebagai alat pembayaran, tetapi juga sebagai instrumen investasi 
dan fondasi berbagai inovasi teknologi seperti DeFi (Decentralized Finance) dan NFT. Namun, crypto juga dikenal memiliki volatilitas tinggi, sehingga memberikan peluang keuntungan besar sekaligus risiko yang signifikan.

</div>
""", unsafe_allow_html=True)

def coin_explanation(coin):
    explanations = {
        "bitcoin": """
🪙 **Bitcoin (BTC)**  
- Crypto pertama & paling stabil  
- Cocok untuk investasi jangka panjang  
- Volatilitas lebih rendah dibanding altcoin  
""",

        "ethereum": """
⚙️ **Ethereum (ETH)**  
- Mendukung smart contract  
- Digunakan untuk DeFi & NFT  
- Lebih fleksibel tapi lebih volatile  
""",

        "solana": """
⚡ **Solana (SOL)**  
- Cepat & biaya rendah  
- Cocok untuk aplikasi skala besar  
- Lebih berisiko (fluktuasi tinggi)  
""",

        "dogecoin": """
🐶 **Dogecoin (DOGE)**  
- Awalnya meme coin  
- Sangat dipengaruhi hype  
- Volatilitas tinggi  
""",

        "binancecoin": """
💰 **Binance Coin (BNB)**  
- Digunakan di ekosistem Binance  
- Stabil karena utility tinggi  
- Bergantung pada platform Binance  
"""
    }

    return explanations.get(coin.lower(), "Informasi tidak tersedia")

if menu == "📊 Market Overview":
    st.markdown("## 📊 Key Metrics")

    last_price = subset_price[coin].iloc[-1]
    prev_price = subset_price[coin].iloc[-2]
    delta = ((last_price - prev_price) / prev_price) * 100

    volatility = df_log[coin].std()
    daily_return = df_log[coin].iloc[-1]

    arrow_up = """
    <svg width="16" height="16" fill="#22c55e" viewBox="0 0 24 24">
    <path d="M4 12l1.41 1.41L11 7.83V20h2V7.83l5.59 5.58L20 12l-8-8-8 8z"/>
    </svg>
    """

    arrow_down = """
    <svg width="16" height="16" fill="#ef4444" viewBox="0 0 24 24">
    <path d="M20 12l-1.41-1.41L13 16.17V4h-2v12.17l-5.58-5.59L4 12l8 8 8-8z"/>
    </svg>
    """
    
    arrow = arrow_up if delta > 0 else arrow_down
    # arrow = "⬆️" if delta > 0 else "⬇️"
    color = "#22c55e" if delta > 0 else "#ef4444"
    bg = "rgba(34,197,94,0.15)" if delta > 0 else "rgba(239,68,68,0.15)"
    market_status = "Bullish 🟢" if delta > 0 else "Bearish 🔴"

    col1, col2, col3, col4 = st.columns(4)

    # CURRENT PRICE
    col1.markdown(f"""
    <div style='padding:18px; background:#020617; border-radius:16px;
    box-shadow: 0 0 15px rgba(56,189,248,0.15);'>

    <div style='color:#94a3b8;'>Current Price</div>
    <div style='font-size:30px;'>${last_price:,.2f}</div>

    <div style='display:inline-block; padding:6px 12px;
    border-radius:20px; background:{bg}; color:{color};'>
    {arrow} {abs(delta):.2f}%
    </div>

    </div>
    """, unsafe_allow_html=True)

    # VOLATILITY
    col2.markdown(f"""
    <div style='padding:18px; background:#020617; border-radius:16px;'>
    <div style='color:#94a3b8;'>Volatility</div>
    <div style='font-size:28px;'>{volatility:.4f}</div>
    </div>
    """, unsafe_allow_html=True)

    # DAILY RETURN
    col3.markdown(f"""
    <div style='padding:18px; background:#020617; border-radius:16px;'>
    <div style='color:#94a3b8;'>Daily Return</div>
    <div style='font-size:28px;'>{daily_return:.4f}</div>
    </div>
    """, unsafe_allow_html=True)

    # MARKET STATUS
    col4.markdown(f"""
    <div style='padding:18px; background:#020617; border-radius:16px;'>
    <div style='color:#94a3b8;'>Market Status</div>
    <div style='font-size:28px; color:{color};'>{market_status}</div>
    </div>
    """, unsafe_allow_html=True)

    # ✅ TARUH DI SINI
    st.markdown("## 📘 About This Coin")
    st.markdown(coin_explanation(coin))
    
    st.markdown("## 📈 Price Movement")

    fig, ax = plt.subplots(figsize=(10, 4))

    ax.set_facecolor('#0e1117')
    fig.patch.set_facecolor('#0e1117')

    ax.plot(subset_price["timestamp"], subset_price[coin], color='#00d4ff', linewidth=1)

    ax.fill_between(
        subset_price["timestamp"],
        subset_price[coin],
        color='#00d4ff',
        alpha=0.1
    )

    ax.tick_params(axis='x', colors='white', labelsize=8)
    ax.tick_params(axis='y', colors='white', labelsize=8)

    ax.spines['bottom'].set_color('white')
    ax.spines['left'].set_color('white')

    st.pyplot(fig)
# =========================
# PERFORMANCE
# =========================
elif menu == "📈 Performance":

    last_price = subset_price[coin].iloc[-1]
    prev_price = subset_price[coin].iloc[-2]
    delta = ((last_price - prev_price) / prev_price) * 100

    st.subheader("📈 Cumulative Return (90 Days)")
    st.line_chart(df_cum.set_index("timestamp"))

    st.markdown("## 📈 Trend Analysis")

    trend = "Bullish 📈" if delta > 0 else "Bearish 📉"

    st.write(f"Current Trend: **{trend}**")

    if delta > 0:
        st.success("Market menunjukkan kenaikan harga.")
    else:
        st.error("Market sedang mengalami penurunan.")
# =========================
# CORRELATION
# =========================
elif menu == "🔥 Correlation":
    st.subheader("🔥 Correlation Heatmap")

    corr = df_log.corr()

    fig, ax = plt.subplots(figsize=(6, 4))

    sns.heatmap(
        corr,
        annot=True,
        cmap="RdYlGn",
        ax=ax,
        linewidths=0.3,
        linecolor='gray',
        cbar=True
    )
    
    ax.set_facecolor("#020617")
    fig.patch.set_facecolor("#020617")
    
    # 🔥 INI YANG BIKIN NAMA KELUAR
    ax.set_xticklabels(ax.get_xticklabels(), rotation=45, color='white')
    ax.set_yticklabels(ax.get_yticklabels(), rotation=0, color='white')
    
    ax.tick_params(axis='x', labelsize=10)
    ax.tick_params(axis='y', labelsize=10)
    
    ax.set_title("Correlation Heatmap (Log Return)", color="white")
    
    st.pyplot(fig)

# =========================
# INSIGHTS
# =========================
elif menu == "🧠 Insights":
    st.subheader("🧠 AI Market Analysis")

    corr = df_log.corr()

    corr_pairs = corr.unstack().sort_values(ascending=False)
    corr_pairs = corr_pairs[corr_pairs < 1]

    highest = corr_pairs.index[0]
    lowest = corr_pairs.index[-1]

    st.markdown(f"""
    ### 🔍 Market Insight

    - 🔗 Korelasi terkuat: **{highest[0]} & {highest[1]}**
    - ⚡ Korelasi terlemah: **{lowest[0]} & {lowest[1]}**

    💡 **Analisis:**
    Pasar crypto menunjukkan hubungan yang kuat antar aset, menandakan adanya pengaruh sentimen global yang sama.

    📊 Bitcoin cenderung menjadi acuan utama, sementara altcoin memiliki volatilitas lebih tinggi.
    """)
    
# =========================

elif menu == "🔮 Trend Analysis":

    st.subheader("🔮 Trend Analysis")

    returns = df_log[coin].dropna()

    avg_return = returns.mean()
    volatility = returns.std()

    trend = "Bullish 📈" if avg_return > 0 else "Bearish 📉"

    col1, col2 = st.columns(2)

    col1.metric("Average Return", f"{avg_return:.5f}")
    col2.metric("Volatility", f"{volatility:.5f}")

    st.markdown("---")

    st.markdown(f"### 📊 Market Condition: {trend}")

    if avg_return > 0:
        st.success("Market cenderung naik.")
    else:
        st.error("Market cenderung turun.")

    st.line_chart(returns)

elif menu == "💰 Portfolio Simulator":

    st.subheader("💰 Investment Simulator")

    investment = st.number_input("Modal Investasi ($)", value=100)
    days = st.slider("Berapa hari lalu beli?", 1, 90, 7)

    prices = df_price[["timestamp", coin]].dropna().set_index("timestamp")

    past_price = prices.iloc[-days][coin]
    current_price = prices.iloc[-1][coin]

    coins_bought = investment / past_price
    current_value = coins_bought * current_price

    profit = current_value - investment
    percent = (profit / investment) * 100

    col1, col2 = st.columns(2)

    col1.write(f"Harga beli: ${past_price:.2f}")
    col1.write(f"Harga sekarang: ${current_price:.2f}")

    color = "green" if profit > 0 else "red"

    col2.markdown(f"""
<div style='font-size:28px; color:{color};'>
${profit:.2f}
</div>
""", unsafe_allow_html=True)

    st.metric("Return (%)", f"{percent:.2f}%")

    if profit > 0:
        st.success("Investasi kamu untung 🚀")
    else:
        st.error("Investasi kamu rugi 📉")
        
st.markdown("---")
st.subheader("🤖 Crypto Assistant")

user_q = st.text_input("Tanya sesuatu... (contoh: crypto terbaik?)")

if user_q:
    q = user_q.lower()

    if "terbaik" in q:
        st.write("💡 Bitcoin stabil, tapi Solana punya growth tinggi.")
    elif "beli" in q:
        st.write("📊 Cek trend & volatility dulu sebelum beli.")
    elif "turun" in q:
        st.write("📉 Market lagi bearish, ini normal di crypto.")
    elif "risiko" in q:
        st.write("⚠️ Altcoin lebih volatile dibanding Bitcoin.")
    else:
        st.write("🤖 Aku sarankan lihat correlation & performance dulu.")
        
def ai_response(q):
    q = q.lower()

    if "heatmap" in q:
        return "Heatmap menunjukkan hubungan antar crypto. Warna hijau = korelasi tinggi, merah = rendah."

    elif "trend" in q:
        return "Trend menunjukkan arah pergerakan harga saat ini, apakah bullish atau bearish."

    elif "bitcoin" in q:
        return "Bitcoin adalah crypto paling stabil dan sering jadi acuan market."

    else:
        return "Coba tanya tentang trend, heatmap, atau crypto tertentu ya!"
        
# =========================
# MANUAL REFRESH BUTTON
# =========================
if st.button("🔄 Refresh Data"):
    st.rerun()

# =========================
# AUTO REFRESH (SAFE)
# =========================
def get_live_price(coin):
    try:
        url = "https://api.coingecko.com/api/v3/simple/price"
        params = {"ids": coin, "vs_currencies": "usd"}
        return requests.get(url, params=params).json()[coin]["usd"]
    except:
        return None
live_price = get_live_price(coin)

if live_price:
    st.metric("💰 Live Price", f"${live_price:,.2f}")
else:
    st.warning("⚠️ Gagal ambil live price (rate limit)")
st.caption("⏱ Auto-refresh setiap 60 detik")
if st.checkbox("🔁 Auto Refresh"):
    time.sleep(10)
    st.rerun()
    
st.markdown("---")
st.container()
