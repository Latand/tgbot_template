from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup,\
    InlineKeyboardButton
from typing import List


def default_kb_admin() -> ReplyKeyboardMarkup:
    kb: List[List[KeyboardButton]] = [[KeyboardButton(text=f'Option_{i}') for i in range(1, 5)]]
    def_kb: ReplyKeyboardMarkup = ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
    return def_kb


def default_kb_stars() -> ReplyKeyboardMarkup:
    kb: List[List[KeyboardButton]] = [[], []]
    kb[0].append(KeyboardButton(text='Расписание уроков 📆'))
    kb[0].append(KeyboardButton(text='Мероприятия 🎉🎉'))
    kb[0].append(KeyboardButton(text='Когда стипендия 💸'))
    kb[1].append(KeyboardButton(text='Вопросы ❓❓'))
    kb[1].append(KeyboardButton(text='Обратная связь 📞'))
    def_kb: ReplyKeyboardMarkup = ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
    return def_kb


def default_kb_men() -> ReplyKeyboardMarkup:
    kb: List[List[KeyboardButton]] = [[KeyboardButton(text=f'Option_{i}_men') for i in range(1, 5)]]
    def_kb: ReplyKeyboardMarkup = ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
    return def_kb


def default_kb_women() -> ReplyKeyboardMarkup:
    kb: List[List[KeyboardButton]] = [[KeyboardButton(text=f'Option_{i}_women') for i in range(1, 5)]]
    def_kb: ReplyKeyboardMarkup = ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
    return def_kb
