import typing

from aiogram.filters import BaseFilter
from aiogram.types import Message

from tgbot.config import Config


class AdminFilter(BaseFilter):
    key = 'is_admin'

    def __init__(self, is_admin: typing.Optional[bool] = None):
        self.is_admin = is_admin

    async def __call__(self, obj: Message) -> bool:
        if self.is_admin is None:
            return False
        #  ToDO: make config work
        # config: Config = obj.bot.get('config')
        admins = [811841340]
        # return (obj.from_user.id in config.tg_bot.admin_ids) == self.is_admin
        return (obj.from_user.id in admins) == self.is_admin

