from typing import Dict, List, Optional, Union

from fastapi import FastAPI

from api import scraper

app = FastAPI()
SCRAPER = scraper.Scraper()


@app.get("/recommendation")
def get_recommendation():
    return SCRAPER.recommendation(api=1)


@app.get("/data")
def get_data(ticker, n_days=30):
    return SCRAPER.get_json(ticker_str=ticker, n_days=n_days)
