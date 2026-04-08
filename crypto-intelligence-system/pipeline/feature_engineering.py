import pandas as pd

df = pd.read_csv("data/crypto_data.csv")

df = df.sort_values(by=["coin", "date"])

print("Missing value awal:")
print(df.isnull().sum())

# Feature
df["return"] = df.groupby("coin")["price"].pct_change()

df["volatility_7d"] = df.groupby("coin")["return"].rolling(7).std().reset_index(0, drop=True)

df["ma_7"] = df.groupby("coin")["price"].rolling(7).mean().reset_index(0, drop=True)
df["ma_30"] = df.groupby("coin")["price"].rolling(30).mean().reset_index(0, drop=True)

print("Sebelum drop:", len(df))

df = df.dropna()

print("Setelah drop:", len(df))

df.to_csv("data/clean_crypto_data.csv", index=False)

print("✅ Data siap analisis!")