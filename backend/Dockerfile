# Используем официальный образ Python
FROM python:3.11-slim

# Рабочая директория внутри контейнера
WORKDIR /app

# Копируем зависимости и ставим их
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копируем весь код
COPY . .

# Открываем порт, по которому будет слушать FastAPI/Uvicorn
EXPOSE 8000

# Переменная окружения для отключения буферизации (чтобы логи шли сразу)
ENV PYTHONUNBUFFERED=1

# Команда запуска вашего приложения (скорректируйте, если у вас другая точка входа)
CMD ["uvicorn", "main:app", "--host", "localhost", "--port", "8000"]