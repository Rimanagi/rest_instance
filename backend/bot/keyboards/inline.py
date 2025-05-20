from aiogram.utils.keyboard import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.types import WebAppInfo

from backend.config import HTTPS_URL

welcome_keyboard = [
    [InlineKeyboardButton(text='Старт', web_app=WebAppInfo(url=HTTPS_URL))],
]
get_welcome_keyboard = InlineKeyboardMarkup(inline_keyboard=welcome_keyboard)
