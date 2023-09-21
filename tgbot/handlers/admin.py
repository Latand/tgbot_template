from aiogram import Dispatcher, Router, F
from aiogram.types import Message
from aiogram import types
from aiogram.filters.command import Command

import json

from tgbot.keyboards.reply import default_kb
from tgbot.filters.admin import AdminFilter, SuperAdminFilter


router = Router()


@router.message(Command(commands=["start"]), AdminFilter(True))
async def admin_start(message: Message):
    with open("tgbot/message_text/start.json", "r") as f:
        json_data: str = f.read()
        text: dict = json.loads(json_data)
    msg: str = text["admin_start"]
    await message.reply(msg, reply_markup=default_kb())


@router.callback_query(F.text.startswith("access"), SuperAdminFilter(True))
async def give_access(callback_query: types.CallbackQuery):
    answer = callback_query.data.split('_')[1].split('-')[0]
    if answer == "allow":
        with open("users.json", "r") as file:
            users_list = json.load(file)
        users_list.append(int(callback_query.data.split('_')[1].split('-')[1]))
        with open("users.json", "w") as f:
            json.dump(users_list, f, indent=4)
