from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup,\
    InlineKeyboardButton

from typing import List
import json


def schedule_stars_kb() -> InlineKeyboardMarkup:
    kb: List[List[InlineKeyboardButton]] = [[]]
    with open("tgbot/message_text/stars/kbs.json", "r") as f:
        text: dict = json.load(f)
    kb[0].append(InlineKeyboardButton(text=text["schedule"]["option_1"], callback_data="schedule_0"))
    kb[0].append(InlineKeyboardButton(text=text["schedule"]["option_2"], callback_data="schedule_1"))
    def_kb: InlineKeyboardMarkup = InlineKeyboardMarkup(inline_keyboard=kb, resize_keyboard=True)
    return def_kb
