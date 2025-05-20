import os

from dotenv import load_dotenv

from aiogram import Bot, Dispatcher
from backend.bot.handlers.start import router

load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")

dp = Dispatcher()
dp.include_router(router)
bot = Bot(token=TOKEN)


async def run_bot():
    print("[BOT] Запускается бот...")
    try:
        await dp.start_polling(bot)
    except Exception as e:
        print(f"[BOT ERROR] {e}")


async def stop_bot():
    await bot.session.close()

# отдельный запуск бота
# import asyncio
# asyncio.run(run_bot())