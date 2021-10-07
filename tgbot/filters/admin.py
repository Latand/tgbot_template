import typing

from aiogram.dispatcher.filters import BoundFilter

from tgbot.config import Config
from tgbot.models.users import User


class AdminFilter(BoundFilter):
    key = 'is_admin'

    def __init__(self, is_admin: typing.Optional[bool] = None):
        self.is_admin = is_admin

    async def check(self, obj):
        """Фильтр для проверки на администратора"""
        session_maker = obj.bot.get('db')
        row = await User.get_user(session_maker, obj.from_user.id)
        return row.admin
