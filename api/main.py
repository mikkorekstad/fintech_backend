from typing import Dict, List, Optional, Union

from fastapi import FastAPI
from pydantic import BaseModel

from api import scraper


class DataRequest(BaseModel):
    ticker_name: str = "^VIX"
    n_days: int = 30


app = FastAPI()
SCRAPER = scraper.Scraper()


@app.get("/recommendation")
def get_recommendation():
    return SCRAPER.recommendation(api=1)


@app.post("/data/")
def get_data(data: DataRequest):
    return SCRAPER.get_json(ticker_str=data.ticker_name, n_days=data.n_days)
