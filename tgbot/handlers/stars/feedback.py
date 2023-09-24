from aiogram import Dispatcher, Router, Bot, types, F
from aiogram.filters.command import Command
from aiogram.fsm.context import FSMContext
from aiogram.utils.markdown import hcode
from tgbot.keyboards.start_kbs import default_kb_stars

import json

from tgbot.misc.stars_states import Feedback
from tgbot.database.database_stars import write_feedback


router: Router = Router()


@router.message(F.text == "Обратная связь 📞")
async def feedback(message: types.Message, state: FSMContext):
    with open("tgbot/message_text/stars/ms_stars.json", "r", encoding="utf-8") as f:
        text: dict = json.load(f)
    msg: str = text["from_main_menu"]["feedback"]["start"]
    await message.answer(msg)
    await state.set_state(Feedback.send)


@router.message(Feedback.send)
async def feedback_send(message: types.Message, state: FSMContext):
    fdbck: str = message.text
    with open("tgbot/message_text/stars/ms_stars.json", "r", encoding="utf-8") as f:
        text: dict = json.load(f)
    write_feedback(fdbck)
    msg: str = text["from_main_menu"]["feedback"]["finish"]
    await message.answer(msg, reply_markup=default_kb_stars())
    await state.clear()
