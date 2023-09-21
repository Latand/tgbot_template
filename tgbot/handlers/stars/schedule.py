from aiogram import Dispatcher, Router, Bot, types, F
from aiogram.filters.command import Command
from aiogram.fsm.context import FSMContext
from aiogram.utils.markdown import hcode
from tgbot.keyboards.stars_kb.stars_from_main import schedule_stars_kb

import json


router = Router()


@router.message(F.text == "Расписание уроков 📆")
async def schedule(message: types.Message):
    with open("tgbot/message_text/stars/ms_stars.json", "r") as f:
        text: dict = json.load(f)
    msg: str = text["from_main_menu"]["schedule"]
    await message.answer(msg, reply_markup=schedule_stars_kb())
