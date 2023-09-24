from aiogram import Dispatcher, Router, Bot, types, F
from aiogram.filters.command import Command
from aiogram.fsm.context import FSMContext
from aiogram.utils.markdown import hcode
from tgbot.keyboards.stars_kb.stars_from_main import schedule_stars_kb

import json

from tgbot.misc.stars_states import Faq
from tgbot.database.database_stars import get_faq


router: Router = Router()


@router.message(F.text == "Вопросы ❓❓")
async def faq(message: types.Message, state: FSMContext):
    with open("tgbot/message_text/stars/ms_stars.json", "r", encoding="utf-8") as f:
        text: dict = json.load(f)
    msg: str = text["from_main_menu"]["questions"]["msg"]
    await message.answer(msg, reply_markup=schedule_stars_kb("FAQ"))
    await state.set_state(Faq.type)


@router.callback_query(Faq.type, F.data.startswith("FAQ"))
async def faq_type_choose(callback_query: types.CallbackQuery, state: FSMContext):
    question = int(callback_query.data.split('_')[1])
    msg: str = get_faq(question)
    await callback_query.message.answer(msg)
    await callback_query.answer()
    await state.clear()
