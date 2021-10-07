from aiogram import Dispatcher

from tgbot.handlers.users.start import register_start


def setup_users(dp: Dispatcher):
    register_start(dp)