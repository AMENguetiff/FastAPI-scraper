from fastapi import FastAPI
from fastapi.responses import JSONResponse
from scraper import scrape_data

app = FastAPI()

@app.get("/scrape/{page_url}")
async def scrape(page_url: str, username: str, password: str):
    try:
        # Call the scraping function with appropriate credentials
        scrape_data(username, password, page_url)
        return {"message": "Scraping completed successfully"}

    except Exception as e:
        return JSONResponse(status_code=500, content={"message": str(e)})
