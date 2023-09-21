from aiogram import Dispatcher, Router, F
from aiogram.types import Message
from aiogram import types
from aiogram.filters.command import Command

import json

from tgbot.keyboards.start_kbs import default_kb_admin, default_kb_stars, default_kb_women, default_kb_men
from tgbot.filters.groups import AdminFilter, SuperAdminFilter, StarsFilter, MenFilter, WomenFilter


router = Router()


@router.message(Command(commands=["start"]), AdminFilter(True))
async def admin_start(message: Message):
    with open("tgbot/message_text/start.json", "r") as f:
        text: dict = json.load(f)
    msg: str = text["admin_start"]
    await message.reply(msg, reply_markup=default_kb_admin())


@router.message(Command(commands=["start"]), StarsFilter(True))
async def stars_start(message: Message):
    with open("tgbot/message_text/start.json", "r") as f:
        text: dict = json.load(f)
    msg: str = text["stars_start"]
    await message.reply(msg, reply_markup=default_kb_stars())


@router.message(Command(commands=["start"]), MenFilter(True))
async def men_start(message: Message):
    with open("tgbot/message_text/start.json", "r") as f:
        text: dict = json.load(f)
    msg: str = text["men_start"]
    await message.reply(msg, reply_markup=default_kb_men())


@router.message(Command(commands=["start"]), WomenFilter(True))
async def women_start(message: Message):
    with open("tgbot/message_text/start.json", "r") as f:
        text: dict = json.load(f)
    msg: str = text["women_start"]
    await message.reply(msg, reply_markup=default_kb_women())
