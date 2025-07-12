import streamlit as st
import pandas as pd
from prophet import Prophet
import matplotlib.pyplot as plt

st.set_page_config(page_title="CrowdPulse Dashboard", layout="wide")
st.title("📡 CrowdPulse: Real-Time Crowd Surge Detection Using AI")

# Upload section
uploaded_file = st.file_uploader("📤 Upload Wi-Fi Log CSV", type="csv")

if uploaded_file:
    # Read and preprocess
    df = pd.read_csv(uploaded_file)
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    df['minute'] = df['timestamp'].dt.floor('min')

    # Aggregate: unique device count per zone per minute
    zone_counts = df.groupby(['minute', 'zone'])['device_id'].nunique().unstack(fill_value=0)
    zone_counts.reset_index(inplace=True)
    st.subheader("📊 Aggregated Device Count per Zone per Minute")
    st.dataframe(zone_counts.tail())

    # Forecast + Surge Detection for each zone
    forecast_minutes = 10
    for zone in zone_counts.columns[1:]:
        st.markdown(f"---\n### 🔮 Zone {zone} Forecast + Surge Detection")

        data = zone_counts[['minute', zone]].rename(columns={'minute': 'ds', zone: 'y'})
        model = Prophet(daily_seasonality=False, weekly_seasonality=False, yearly_seasonality=False)
        model.fit(data)

        future = model.make_future_dataframe(periods=forecast_minutes, freq='min')
        forecast = model.predict(future)

        # Merge for detection
        full = forecast[['ds', 'yhat']].copy()
        full = full.merge(data, on='ds', how='left')

        # Rolling stats
        recent = full[~full['y'].isna()].copy()
        mean_recent = recent['y'].rolling(15, min_periods=5).mean().iloc[-1]
        std_recent = recent['y'].rolling(15, min_periods=5).std().iloc[-1]
        threshold = mean_recent + 2 * std_recent

        # Detect surge
        future_df = full[-forecast_minutes:]
        surges = future_df[future_df['yhat'] > threshold]
        surge_times = surges['ds'].tolist()

        # Plot
        fig = model.plot(forecast)
        plt.axhline(threshold, color='red', linestyle='--', label='Surge Threshold')
        plt.title(f"Zone {zone} — Forecast with Surge Threshold")
        plt.legend()
        st.pyplot(fig)

        # Show alerts
        if surge_times:
            st.error(f"🚨 Surge expected in Zone {zone} at:\n" +
                     '\n'.join(t.strftime('%H:%M') for t in surge_times))
        else:
            st.success(f"✅ No surge predicted in Zone {zone}")
