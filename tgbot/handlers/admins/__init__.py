from aiogram import Dispatcher

from tgbot.handlers.admins.admin import register_admin_start


def setup_admins(dp: Dispatcher):
    register_admin_start(dp)