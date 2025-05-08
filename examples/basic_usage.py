import pandas as pd
from grafanapy import start_server

df = pd.DataFrame({
    "time": pd.date_range(end=pd.Timestamp.now(), periods=10, freq="H"),
    "value": [x**0.5 for x in range(10)]
})

start_server(df, port=8000)
