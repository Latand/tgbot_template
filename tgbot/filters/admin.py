import typing

from aiogram.filters import BaseFilter
from aiogram.types import Message

from tgbot.config import Config_settings


class AdminFilter(BaseFilter):
    key = 'is_admin'

    def __init__(self, is_admin: typing.Optional[bool] = None):
        self.is_admin = is_admin

    async def __call__(self, obj: Message) -> bool:
        if self.is_admin is None:
            return False
        config: Config = Config_settings
        return (obj.from_user.id in config.tg_bot.admin_ids) == self.is_admin


class SuperAdminFilter(BaseFilter):
    key = 'is_super_admin'

    def __init__(self, is_super_admin: typing.Optional[bool] = None):
        self.is_super_admin = is_super_admin

    async def __call__(self, obj: Message) -> bool:
        if self.is_super_admin is None:
            return False
        config: Config = Config_settings
        return (obj.from_user.id == config.tg_bot.super_admin_ids) == self.is_super_admin
