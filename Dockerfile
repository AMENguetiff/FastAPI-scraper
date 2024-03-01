# Use an official Python runtime as a parent image
FROM python:3.11.2

# Set the working directory in the container
WORKDIR /app

COPY . /app

# Install the Python dependencies
RUN pip install -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 8080

# Run fastapi_app.py when the container launches
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
