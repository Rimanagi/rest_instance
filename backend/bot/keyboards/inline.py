from aiogram.utils.keyboard import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.types import WebAppInfo

from backend.config import URL


welcome_keyboard = [
    [InlineKeyboardButton(text='Старт', web_app=WebAppInfo(url='https://google.com'))],
]
get_welcome_keyboard = InlineKeyboardMarkup(inline_keyboard=welcome_keyboard)
