from typing import Dict, List, Optional, Union

from fastapi import FastAPI

import scraper

app = FastAPI()
SCRAPER = scraper.Scraper()


@app.get("/recommendation")
def get_recommendation():
    return SCRAPER.recommendation(api=1)
