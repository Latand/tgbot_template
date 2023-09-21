from aiogram import Router, Bot
from aiogram.filters.command import Command
from aiogram.types import Message

import json

from tgbot.keyboards.inline import give_access_kb
from tgbot.config import Config_settings


router = Router()


@router.message(Command(commands=["start"]))
async def user_start(message: Message, bot: Bot):
    with open("users.json", "r") as file:
        users_list = json.load(file)
    if message.from_user not in users_list:
        config: Config = Config_settings
        await bot.send_message(config.tg_bot.super_admin_ids, "User wants access", reply_markup=give_access_kb(message.from_user.id))
    await message.reply("Hello, user!")
