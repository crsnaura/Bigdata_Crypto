import requests
import pandas as pd
import time

coins = ["bitcoin", "ethereum", "solana", "dogecoin", "binancecoin"]

all_data = []

for coin in coins:
    print(f"Ambil data {coin}...")

    url = f"https://api.coingecko.com/api/v3/coins/{coin}/market_chart"

    params = {
        "vs_currency": "usd",
        "days": "90"
    }

    response = requests.get(url, params=params)
    data = response.json()

    prices = data["prices"]
    market_caps = data["market_caps"]
    volumes = data["total_volumes"]

    df_price = pd.DataFrame(prices, columns=["timestamp", "price"])
    df_market = pd.DataFrame(market_caps, columns=["timestamp", "market_cap"])
    df_volume = pd.DataFrame(volumes, columns=["timestamp", "volume"])

    df = df_price.merge(df_market, on="timestamp")
    df = df.merge(df_volume, on="timestamp")

    df["coin"] = coin

    all_data.append(df)

    time.sleep(1)

final_df = pd.concat(all_data)

# simpan
final_df.to_csv("data/crypto_data.csv", index=False)

print("✅ Data berhasil disimpan!")