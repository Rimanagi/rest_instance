from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message, FSInputFile, URLInputFile

from backend.config import WELCOME_PICTURE_PATH, CAPTION
from backend.bot.keyboards.inline import get_welcome_keyboard

router = Router()


@router.message(Command("start"))
async def command_start_handler(message: Message) -> None:
    photo_path = str(WELCOME_PICTURE_PATH)

    await message.answer_photo(
        # photo=URLInputFile(url='https://t3.ftcdn.net/jpg/00/87/97/06/360_F_87970620_Tdgw6WYdWnrZHn2uQwJpVDH4vr4PINSc.jpg'),
        photo=FSInputFile(path=photo_path),
        caption=CAPTION,
        reply_markup=get_welcome_keyboard
    )
