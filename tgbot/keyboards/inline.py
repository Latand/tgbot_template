from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, \
    InlineKeyboardButton

import json


def schedule_kb() -> InlineKeyboardMarkup:
    with open("tgbot/message_text/keyboards_text.json", "r") as f:
        json_data: str = f.read()
        text: dict = json.loads(json_data)
    kb = [[InlineKeyboardButton(text=text["schedule"]["inline_1"], callback_data='schedule_lessons')],
          [InlineKeyboardButton(text=text["schedule"]["inline_2"], callback_data='schedule_activities')]]
    return InlineKeyboardMarkup(inline_keyboard=kb)


def give_access_kb(id: int) -> InlineKeyboardMarkup:
    kb = [[InlineKeyboardButton(text="allow", callback_data=f"access_allow-{id}")],
          [InlineKeyboardButton(text="deny", callback_data=f"access_deny-{id}")]]
    return InlineKeyboardMarkup(inline_keyboard=kb)
