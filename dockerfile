FROM python:3.12-bullseye

RUN apt-get update -y && apt-get upgrade -y

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

ENV GEMINI_API_KEY=""

CMD ["python3", "app.py"]