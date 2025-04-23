FROM python:3.13-slim
WORKDIR /app
RUN apt update && apt install -y ffmpeg && apt-get clean && rm -rf /var/lib/apt/lists/* 
COPY . /app
RUN pip install --no-cache-dir -r requirements.txt
CMD ["python3",  "/app/main.py"]
