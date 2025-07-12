import streamlit as st
import pandas as pd
from prophet import Prophet
import matplotlib.pyplot as plt

st.set_page_config(page_title="CrowdPulse Dashboard", layout="wide")
st.title("📡 CrowdPulse: Real-Time Crowd Surge Detection Using AI")

uploaded_file = st.file_uploader("📤 Upload Wi-Fi Log CSV", type="csv")

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    df = df.set_index('timestamp').resample('1min').mean().reset_index()

    st.subheader("📊 Aggregated Device Counts Per Zone")
    st.dataframe(df.tail())

    forecast_minutes = 10

    for zone in df.columns[1:]:
        st.markdown(f"---\n### 🔮 Zone {zone} Forecast + Surge Detection")

        data = df[['timestamp', zone]].rename(columns={'timestamp': 'ds', zone: 'y'})
        model = Prophet(daily_seasonality=False, weekly_seasonality=False, yearly_seasonality=False)
        model.fit(data)

        future = model.make_future_dataframe(periods=forecast_minutes, freq='min')
        forecast = model.predict(future)

        full = forecast[['ds', 'yhat']].copy()
        full = full.merge(data, on='ds', how='left')

        recent = full[~full['y'].isna()].copy()
        mean_recent = recent['y'].rolling(15, min_periods=5).mean().iloc[-1]
        std_recent = recent['y'].rolling(15, min_periods=5).std().iloc[-1]
        threshold = mean_recent + 2 * std_recent

        future_df = full[-forecast_minutes:]
        surges = future_df[future_df['yhat'] > threshold]
        surge_times = surges['ds'].tolist()

        fig = model.plot(forecast)
        plt.axhline(threshold, color='red', linestyle='--', label='Surge Threshold')
        plt.title(f"Zone {zone} — Forecast with Surge Threshold")
        plt.legend()
        st.pyplot(fig)

        if surge_times:
            st.error(f"🚨 Surge expected in Zone {zone} at:\n" +
                     '\n'.join(t.strftime('%H:%M') for t in surge_times))
        else:
            st.success(f"✅ No surge predicted in Zone {zone}")
