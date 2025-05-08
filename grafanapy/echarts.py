import pandas as pd

def generate_line_chart(df: pd.DataFrame, x_col: str, y_col: str) -> dict:
    return {
        "xAxis": {
            "type": "category",
            "data": df[x_col].astype(str).tolist()
        },
        "yAxis": {
            "type": "value"
        },
        "series": [{
            "data": df[y_col].tolist(),
            "type": "line",
            "smooth": True
        }]
    }

def generate_bar_chart(df: pd.DataFrame, x_col: str, y_col: str) -> dict:
    return {
        "xAxis": {
            "type": "category",
            "data": df[x_col].astype(str).tolist()
        },
        "yAxis": {
            "type": "value"
        },
        "series": [{
            "data": df[y_col].tolist(),
            "type": "bar"
        }]
    }

def generate_pie_chart(df: pd.DataFrame, label_col: str, value_col: str) -> dict:
    return {
        "tooltip": {
            "trigger": "item"
        },
        "series": [{
            "type": "pie",
            "radius": "50%",
            "data": [
                {"value": row[value_col], "name": row[label_col]}
                for _, row in df.iterrows()
            ],
            "emphasis": {
                "itemStyle": {
                    "shadowBlur": 10,
                    "shadowOffsetX": 0,
                    "shadowColor": "rgba(0, 0, 0, 0.5)"
                }
            }
        }]
    }
