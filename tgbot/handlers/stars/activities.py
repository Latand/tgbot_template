from aiogram import Dispatcher, Router, Bot, types, F
from aiogram.filters.command import Command
from aiogram.fsm.context import FSMContext
from aiogram.utils.markdown import hcode
from tgbot.keyboards.stars_kb.stars_from_main import schedule_stars_kb

import json

from tgbot.misc.stars_states import Activities
from tgbot.database.database_stars import get_activities


router: Router = Router()


@router.message(F.text == "Мероприятия 🎉🎉")
async def activities(message: types.Message, state: FSMContext):
    with open("tgbot/message_text/stars/ms_stars.json", "r", encoding="utf-8") as f:
        text: dict = json.load(f)
    msg: str = text["from_main_menu"]["activities"]
    await message.answer(msg, reply_markup=schedule_stars_kb("activities"))
    await state.set_state(Activities.type)


@router.callback_query(Activities.type, F.data.startswith("activities"))
async def activities_type_choose(callback_query: types.CallbackQuery, state: FSMContext):
    activities_types: dict = {
        "0": "nearest"
    }
    activities_type: str = callback_query.data.split('_')[1]
    response = get_activities(activities_types[activities_type])
    await callback_query.message.answer(response)
    await callback_query.answer()
    await state.clear()
