from aiogram import Dispatcher, Router, Bot, types, F
from aiogram.filters.command import Command
from aiogram.fsm.context import FSMContext
from aiogram.utils.markdown import hcode
from tgbot.keyboards.inline import schedule_kb

import json


router = Router()


@router.message(F.text == "schedule")
async def schedule(message: types.Message):
    with open("tgbot/message_text/main_menu.json", "r") as f:
        json_data: str = f.read()
        text: dict = json.loads(json_data)
    msg: str = text["choose_type_of_schedule"]

    await message.answer(msg, reply_markup=schedule_kb())


@router.message(F.text == "asdas")
async def bot_echo_all(message: types.Message, state: FSMContext):
    state_name = await state.get_state()
    text = [
        f'Эхо в состоянии {hcode(state_name)}',
        'Содержание сообщения:',
        hcode(message.text)
    ]
    await message.answer('\n'.join(text))


@router.callback_query(F.text.startswith("schedule"))
async def schedule_type_choose(callback_query: types.CallbackQuery):
    print(callback_query.data)
