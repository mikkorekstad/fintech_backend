from typing import Dict, List, Optional, Union
from api.ticker_model_manager import Ticker

from fastapi import FastAPI
from pydantic import BaseModel

from api import scraper
from api import model


new_day = True # is it a new day?
selected_ticker = Ticker.SP500 # ticker to be analyzed
print(selected_ticker.value)
# Check if 
if new_day:
    pass
    # get data new
    # Train model
    # set flag to false
    # check if ticker is in list of models
    # get prediction on spefific ticker if ticker is not trained on create a new model and add to a list of models

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
