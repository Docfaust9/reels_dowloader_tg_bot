FROM python:3.13-slim
WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir -r requirements.txt
RUN apt update && apt install -y ffmpeg && apt-get clean && rm -rf /var/lib/apt/lists/* 
CMD ["python3",  "/app/main.py"]
