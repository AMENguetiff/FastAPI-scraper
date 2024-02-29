# FastAPI-scraper

I developed a comprehensive solution leveraging FastAPI, Uvicorn, and SQLite to create a robust web service capable of scraping and storing data from public Facebook pages. The project comprises several key components.

### 🔍 FastAPI Application

The core of the project is a FastAPI application serving as the entry point for the web service. It defines endpoints to handle incoming requests and execute specific actions, such as triggering the scraping process and retrieving scraped data.

Establishing and configuring a virtual environment (venv) and installing all the necessary requirements. 

   python -m venv venv
   
   pip install [ALL REQUIRMENTS]
   
I utilized Uvicorn, a lightning-fast ASGI server, to run the FastAPI application. Uvicorn's high performance and compatibility with FastAPI ensure optimal performance and scalability for the web service.

uvicorn main:app --reload

### 📝 Scraping Functionality 

Integrated into the FastAPI application is a scraping function responsible for extracting data from public Facebook pages. This function utilizes Selenium to navigate Facebook pages, extract post content, likes, shares, comments count, and user numbers per post.

### 📥 SQLite Database

The scraped data is stored in an SQLite database for persistence. I created a database schema to organize the data efficiently and implemented logic to insert the scraped data into the database tables.

Dockerization: To facilitate deployment and distribution, I dockerized the entire application along with its dependencies. This ensures consistency across different environments and simplifies the deployment process
## 📚 Documentation

For detailed documentation, please visit our [official documentation](https://pypi.org/project/dashboard-dataviz-panel/0.1.3/)
