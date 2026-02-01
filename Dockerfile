FROM python:3.10-slim

ENV PYTHONUNBUFFERED 1 \ 
    PYTHONDONTWRITEBYTECODE 1

WORKDIR /app 

RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/* 

COPY . . 

RUN  pip install --no-cache-dir -e . 

EXPOSE 8501
EXPOSE 8080 

CMD ["python", "-m" , "app.app"]