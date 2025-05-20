import asyncio
from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI, Request
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

templates = Jinja2Templates(directory="docs")
@app.get("/")
async def ping(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


if __name__ == '__main__':
    uvicorn.run("main:app", host=HOST, port=PORT, reload=True)
