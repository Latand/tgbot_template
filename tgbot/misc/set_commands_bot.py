from aiogram import types, Dispatcher
from aiogram.types import BotCommandScopeChat


async def set_commands(dp: Dispatcher):
    await dp.bot.set_my_commands(
        [
            types.BotCommand("start", "Запустить бота"),
            types.BotCommand("help", "Вывести справку"),
        ]
    )
    config: Config = dp.bot.get('config')
    for admin in config.tg_bot.admin_ids:
        await dp.bot.set_my_commands(
            [
                types.BotCommand("appoint_admin", "Назначить себя админом в БД"),
            ],
            BotCommandScopeChat(admin)
        )