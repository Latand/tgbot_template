from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton


def default_kb() -> ReplyKeyboardMarkup:
    kb = [[KeyboardButton(text='schedule')]]
    def_kb: ReplyKeyboardMarkup = ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
    return def_kb
