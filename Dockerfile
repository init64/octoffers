# Использование базового образа Python
FROM python:3.11-slim

# Установка рабочего каталога в контейнере
WORKDIR /app

# Копирование файлов зависимостей и установка зависимостей
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копирование остальных файлов проекта
COPY . .

# Запуск приложения
CMD ["python", "/app/octoffers/main.py"]
