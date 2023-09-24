from aiogram import Dispatcher, Router, Bot, types, F
from aiogram.filters.command import Command
from aiogram.fsm.context import FSMContext
from aiogram.utils.markdown import hcode
from tgbot.keyboards.stars_kb.stars_from_main import schedule_stars_kb

import json

from tgbot.misc.stars_states import Schedule
from tgbot.database.database_stars import get_schedule


router: Router = Router()


@router.message(F.text == "Расписание уроков 📆")
async def schedule(message: types.Message, state: FSMContext):
    with open("tgbot/message_text/stars/ms_stars.json", "r", encoding="utf-8") as f:
        text: dict = json.load(f)
    msg: str = text["from_main_menu"]["schedule"]
    await message.answer(msg, reply_markup=schedule_stars_kb("schedule"))
    await state.set_state(Schedule.type)


@router.callback_query(Schedule.type, F.data.startswith("schedule"))
async def schedule_type_choose(callback_query: types.CallbackQuery, state: FSMContext):
    schedule_type = int(callback_query.data.split('_')[1])
    response: str = get_schedule(schedule_type)
    await callback_query.message.answer(response)
    await callback_query.answer()
    await state.clear()
