import typing
import json

from aiogram.filters import BaseFilter
from aiogram.types import Message

from tgbot.config import Config_settings, Config


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


class StarsFilter(BaseFilter):
    key = 'is_stars'

    def __init__(self, is_stars: typing.Optional[bool] = None):
        self.is_stars = is_stars

    async def __call__(self, obj: Message) -> bool:
        if self.is_stars is None:
            return False
        with open("database/groups.json", "r") as file:
            groups_list = json.load(file)
        stars: typing.List[int] = groups_list["stars"]
        return (obj.from_user.id in stars) == self.is_stars


class MenFilter(BaseFilter):
    key = 'is_men'

    def __init__(self, is_men: typing.Optional[bool] = None):
        self.is_men = is_men

    async def __call__(self, obj: Message) -> bool:
        if self.is_men is None:
            return False
        with open("database/groups.json", "r") as file:
            groups_list = json.load(file)
        men: typing.List[int] = groups_list["men"]
        return (obj.from_user.id in men) == self.is_men


class WomenFilter(BaseFilter):
    key = 'is_women'

    def __init__(self, is_women: typing.Optional[bool] = None):
        self.is_women = is_women

    async def __call__(self, obj: Message) -> bool:
        if self.is_women is None:
            return False
        with open("database/groups.json", "r") as file:
            groups_list = json.load(file)
        women: typing.List[int] = groups_list["women"]
        return (obj.from_user.id in women) == self.is_women
