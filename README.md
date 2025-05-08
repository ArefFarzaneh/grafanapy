# 📊 GrafanaPy

**GrafanaPy** is a Python package that allows you to seamlessly expose a `pandas.DataFrame` via a FastAPI server and visualize it in **Grafana** using the **JSON API** and **ECharts** plugins.

> Perfect for Python developers and data professionals who want to connect their Python data directly to Grafana dashboards.

---

## ✨ Features

- 📦 Serve Pandas DataFrames as JSON endpoints
- ⚡ Auto-generate ECharts configs for quick visualizations
- 🔌 Compatible with Grafana’s JSON API & ECharts plugins
- 🧪 Easy to test locally, no DB or external API required

---

## 📦 Installation

### 1. Clone or Download the Repo

```bash
git clone https://github.com/yourusername/grafanapy.git
cd grafanapy
```


### 2.Install Python Dependencies

```bash
pip install fastapi uvicorn pandas
```

---
### 3. ▶️ Running the Server
Create a test script like test_grafana_server.py

```bash
import pandas as pd
from grafanapy.server import start_server

df = pd.DataFrame({
    "time": pd.date_range(end=pd.Timestamp.now(), periods=10, freq="H"),
    "value": [i**0.5 for i in range(10)]
})

start_server(df)
```
Then run it:
```bash
python test_grafana_server.py
```

You should see:
```bash 
Serving Grafana-compatible data at http://localhost:8000/data and /echarts
```
---

### 4. 📥 Install and Set Up Grafana
[official instructions](https://grafana.com/docs/grafana/latest/setup-grafana/installation/)

Grafana will run at:
[http://localhost:3000](http://localhost:3000)

(Default login: `admin` / `admin`)
---
### 4. 🔌 Install Required Grafana Plugins

✅ JSON API Plugin
📊 ECharts Panel Plugin (Optional)

Restart Grafana if needed:
`sudo systemctl restart grafana-server`

---
### 5.⚙️ Add JSON API as Data Source

Go to Configuration → Data Sources

Click Add data source

Select JSON API

Configuration:
Name	`FastAPI Data`

URL	`http://localhost:8000`

Access	`Server (default)`

