# 🚦 CrowdPulse: Real-Time Crowd Monitoring Using Wi-Fi Probe Logs

📍 **Live App**: [Click to Open](https://crowdpulse-n2kmupxkwfrnchrsshj8fo.streamlit.app/)

## 📊 Overview
CrowdPulse is a real-time crowd monitoring dashboard that analyzes Wi-Fi probe logs to detect and forecast crowd surges in multiple zones. It uses Facebook Prophet to forecast future crowd density and flags anomalies above a dynamic surge threshold.

## 🔧 Features
- 📈 Time-series forecasting for device counts per zone
- 🚨 Surge detection with dynamic thresholds
- 🕒 Minute-level resolution of Wi-Fi logs
- 📉 Visual plots with confidence intervals and anomaly marking

## 🗂️ File Structure

| File | Description |
|------|-------------|
| `app.py` | Main Streamlit app |
| `wifi_probe_log.csv` | Input dataset with timestamped zone counts |
| `requirements.txt` | Python dependencies |

## 🖼️ Sample Visuals

<img src="https://raw.githubusercontent.com/yourusername/crowdpulse/main/sample_forecast_zone_A.png" width="600"/>
<img src="https://raw.githubusercontent.com/yourusername/crowdpulse/main/sample_forecast_zone_C.png" width="600"/>

> 💡 Replace these image URLs with your actual screenshots after uploading them to GitHub!

## ▶️ How to Run Locally

```bash
git clone https://github.com/yourusername/crowdpulse.git
cd crowdpulse
pip install -r requirements.txt
streamlit run app.py
