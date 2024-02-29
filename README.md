# FastAPI-scraper

I utilized Selenium to conduct scraping of various Facebook page contents and then integrated it with FastAPI to offer an API equipped with appropriate credentials for initiating the scraping process.

1. Establishing and configuring a virtual environment (venv) and installing all the necessary requirements. 

   python -m venv venv
   
   pip install [ALL REQUIRMENTS]
2. Creating a main.py file and testing the FastAPI application.

   uvicorn app:main --reload
3. Implementing the complete scraper code in scraper.py and creating db.py to handle the storage of data.

We are now prepared to initiate the data scraping process using FastAPI !
