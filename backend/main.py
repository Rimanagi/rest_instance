import asyncio
from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.templating import Jinja2Templates
from backend.bot.app_tg import run_bot, stop_bot

from config import HOST, PORT


@asynccontextmanager
async def lifespan(app: FastAPI):
    bot_task = asyncio.create_task(run_bot())  # запускаем бота
    yield
    await stop_bot()  # закрываем соединение
    bot_task.cancel()


app = FastAPI(lifespan=lifespan)

# Настройка CORS - разрешаем все origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Разрешаем все домены
    allow_credentials=True,
    allow_methods=["*"],  # Разрешаем все HTTP-методы
    allow_headers=["*"],  # Разрешаем все заголовки
)

@app.get("/")
async def ping(request: Request):
    return { 
        'port': PORT,
        'address': HOST
    }


if __name__ == '__main__':
    uvicorn.run("main:app", host=HOST, port=PORT, reload=True)
