# parent image
FROM python:3.11.2

# Set the working directory in the container
WORKDIR /app

COPY . /app

# Install the Python reqts
RUN pip install -r requirements.txt

# Make port 80 available
EXPOSE 8000

# Run fastapiAPP.py when the container launches
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
