import asyncio
from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI
from backend.bot.app_tg import run_bot, stop_bot

from config import HOST, PORT


@asynccontextmanager
async def lifespan(app: FastAPI):
    bot_task = asyncio.create_task(run_bot())  # запускаем бота
    yield
    await stop_bot()  # закрываем соединение
    bot_task.cancel()


app = FastAPI(lifespan=lifespan)


@app.get("/ping")
async def ping():
    return {"status": "ok"}


if __name__ == '__main__':
    uvicorn.run("main:app", host=HOST, port=PORT, reload=True)
