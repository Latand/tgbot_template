from aiogram import Dispatcher
from aiogram.types import Message

from tgbot.models.users import User


async def admin_start(message: Message):
    await message.reply("Hello, admin!")


async def appoint_admin(message: Message, user: User):
    config: Config = message.bot.get('config')
    if str(message.from_user.id) in config.tg_bot.admin_ids:
        if user.admin:
            return await message.answer('Вы уже являетесь администратором')

        db_session = message.bot.get('db')
        await message.answer('Вы назначали себя администратором')
        await user.update_user(db_session, updated_fields={'admin': True})
        return


def register_admin_start(dp: Dispatcher):
    dp.register_message_handler(admin_start, commands=["start"], state="*", is_admin=True)
    dp.register_message_handler(appoint_admin, commands=["appoint_admin"], state="*")
