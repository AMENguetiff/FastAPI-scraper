# FastAPI-scraper                                                                                      

We can acknowledge that scraping data from Facebook poses unique challenges due to the platform's policies, dynamic page structures, and security measures. However, I've risen to this challenge by developing a comprehensive solution leveraging some advanced technologies. This solution empowers the creation of a robust service capable of efficiently scraping and securely storing data from public Facebook pages. The project encompasses several key components, including a FastAPI application serving as the backbone of the service, Uvicorn for running the application, Selenium for web scraping, and SQLite for database management. Together, these components form a cohesive and scalable solution to tackle the complexities of scraping data from Facebook.  


## 🔍 FastAPI Application

The core of the project is a FastAPI application serving as the entry point for the web service. It defines endpoints to handle incoming requests and execute specific actions, such as triggering the scraping process and retrieving scraped data.

To start we should establish and configure a virtual environment and installing all the necessary requirements. 

   ##### python -m venv venv
   
   ##### pip install [ALL REQUIRMENTS]
   
I utilized Uvicorn, a lightning-fast ASGI server, to run the FastAPI application. Uvicorn's high performance and compatibility with FastAPI ensure optimal performance and scalability for the web service.

   ##### uvicorn main:app --reload

## 📝 Scraping Functionality 

Integrated into the FastAPI application is a scraping function responsible for extracting data from public Facebook pages. This function utilizes Selenium to navigate Facebook pages, extract post content, likes, shares, comments count, and the number of users who commented per post.

## 📥 SQLite Database

The scraped data is stored in an SQLite database for persistence. I created a database schema to organize the data efficiently and implemented logic to insert the scraped data into the database tables.

## ![image](https://github.com/AMENguetiff/FastAPI-scraper/assets/121358015/2468a743-f9bd-43b4-b29b-707f21d43d61) Dockerization

To facilitate deployment and distribution, I dockerized the entire application along with its dependencies. This ensures consistency across different environments and simplifies the deployment process.

## 📚 Documentation

For detailed documentation, please visit https://fastapi.tiangolo.com/

## 📦 Module
In this section, I'll showcase screenshots captured from the localhost after running our FastAPI application.
