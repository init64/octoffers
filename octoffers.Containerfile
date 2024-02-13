FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt && \
  mkdir -p $HOME/.config/octoffers
COPY . .
CMD ["python", "/app/octoffers"]
