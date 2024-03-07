FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt &&\
  mkdir -p $HOME/.config/octoffers
COPY . .
LABEL org.opencontainers.image.source=https://github.com/init64/octoffers
CMD ["python", "/app/octoffers"]
