from fastapi import FastAPI
from fastapi.responses import JSONResponse
import pandas as pd
import uvicorn
from threading import Thread
from .echarts import generate_line_chart

def serve_dataframe(df: pd.DataFrame, path: str = "/data", echarts_path: str = "/echarts") -> FastAPI:
    app = FastAPI()

    @app.get(path)
    def get_data():
        result = df.copy()
        if "time" in result.columns:
            result["time"] = result["time"].astype(str)
        return JSONResponse(content=result.to_dict(orient="records"))

    @app.get(echarts_path)
    def get_echarts_config():
        if "time" in df.columns and "value" in df.columns:
            option = generate_line_chart(df, "time", "value")
            return JSONResponse(content=option)
        return JSONResponse(content={"error": "Missing 'time' or 'value' column"}, status_code=400)

    return app

def start_server(df: pd.DataFrame, port: int = 8000):
    app = serve_dataframe(df)

    def run():
        uvicorn.run(app, host="0.0.0.0", port=port, log_level="info")

    thread = Thread(target=run)
    thread.start()  # not daemon
    print(f"Serving Grafana-compatible data at http://localhost:{port}/data and /echarts")
    thread.join()  # ⬅️ this keeps the script alive
