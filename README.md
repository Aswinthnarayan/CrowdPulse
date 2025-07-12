# 🚦 CrowdPulse: Real-Time Crowd Monitoring Using Wi-Fi Probe Logs

[![Streamlit App](https://img.shields.io/badge/Live%20App-Streamlit-green?style=for-the-badge&logo=streamlit)](https://crowdpulse-n2kmupxkwfrnchrsshj8fo.streamlit.app/)

CrowdPulse is a real-time dashboard that monitors crowd density using Wi-Fi probe logs. It leverages time-series forecasting (Prophet) to detect surges in crowd activity across multiple zones.

---

## 📊 Features
- 📈 Real-time crowd forecasting (per zone)
- 🚨 Surge detection based on thresholds
- 📉 Visual plots with confidence intervals
- 🧠 Uses Facebook Prophet for minute-level analysis
- 🗃️ Simple CSV-based data format

---

## 📂 File Structure

| File | Description |
|------|-------------|
| `app1.py` | Main Streamlit dashboard app |
| `wifi_probe_log.csv` | Sample Wi-Fi probe log data |
| `requirements.txt` | Python dependencies |
| `assets/` | Folder containing screenshot images |
| `README.md` | Project documentation |

---

## ▶️ How to Run Locally

```bash
git clone https://github.com/Aswinthnarayan/CrowdPulse.git
cd CrowdPulse
pip install -r requirements.txt
streamlit run app1.py

