import pandas as pd
import numpy as np

df = pd.read_csv("data/crypto_data.csv")

# convert timestamp
df["timestamp"] = pd.to_datetime(df["timestamp"], unit="ms")

# pivot
df_pivot = df.pivot(index="timestamp", columns="coin", values="price")

# resample
df_hourly = df_pivot.resample("1h").last().ffill()

# log return
df_log_return = np.log(df_hourly / df_hourly.shift(1))

# cumulative return
df_cum_return = df_hourly.copy()

for col in df_cum_return.columns:
    first_valid = df_cum_return[col].dropna().iloc[0]
    df_cum_return[col] = (df_cum_return[col] / first_valid - 1) * 100

# save
df_hourly.to_csv("data/hourly_price.csv")
df_log_return.to_csv("data/log_return.csv")
df_cum_return.to_csv("data/cum_return.csv")

print("✅ Advanced data ready!")