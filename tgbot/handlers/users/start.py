from aiogram import Dispatcher
from aiogram.types import Message


from tgbot.models.users import User


async def user_start(message: Message, user: User):
    await message.reply("Hello, user!")


def register_start(dp: Dispatcher):
    dp.register_message_handler(user_start, commands=["start"], state="*")
