df["timestamp"] = pd.to_datetime(df["timestamp"], unit="ms")

df_pivot = df.pivot(index="timestamp", columns="coin_name", values="price")

df_hourly = df_pivot.resample("1h").last().ffill()

df_log_return = np.log(df_hourly / df_hourly.shift(1))

df_cum_return = df_hourly.copy()
for col in df_cum_return.columns:
    first_valid = df_cum_return[col].dropna().iloc[0]
    df_cum_return[col] = (df_cum_return[col] / first_valid - 1) * 100
