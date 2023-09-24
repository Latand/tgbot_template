from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup,\
    InlineKeyboardButton

from typing import List
import json


def schedule_stars_kb(key: str) -> InlineKeyboardMarkup:
    kb: List[List[InlineKeyboardButton]] = []
    with open("tgbot/message_text/stars/kbs.json", "r", encoding="utf-8") as f:
        text: dict = json.load(f)[key]
    text_keys = list(text.keys())
    for i in range(len(text_keys)):
        kb.append([])
        kb[i].append(InlineKeyboardButton(text=text[text_keys[i]], callback_data=f"{key}_{i}"))
    def_kb: InlineKeyboardMarkup = InlineKeyboardMarkup(inline_keyboard=kb, resize_keyboard=True)
    return def_kb
