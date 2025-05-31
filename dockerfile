# Use the official Python 3.12 Bullseye image as the base image
FROM python:3.12-bullseye

RUN apt-get update -y && apt-get upgrade -y

RUN apt install -y sqlite3 libsqlite3-dev

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install the Python dependencies

RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code into the container
COPY . .

# Expose port 5000
EXPOSE 5000

# Set up environment variable for Gemini API key
ENV GEMINI_API_KEY=""

# Command to run the Flask application
CMD ["python3", "app.py"]