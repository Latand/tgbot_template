import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
# from aiogram.fsm.storage.redis import RedisStorage

from tgbot.config import Config_settings
from tgbot.filters.groups import AdminFilter
from tgbot.handlers import admin
from tgbot.handlers import echo
from tgbot.handlers import user
from tgbot.handlers import start
from tgbot.handlers.stars import schedule, activities, scholarship, faq, feedback


logger = logging.getLogger(__name__)


def register_all_filters(dp):
    dp.filters_factory.bind(AdminFilter)


async def main():
    logging.basicConfig(
        level=logging.INFO,
        format=u'%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s',
    )
    logger.info("Starting bot")
    config = Config_settings

    storage = MemoryStorage()  # RedisStorage() if config.tg_bot.use_redis else
    bot = Bot(token=config.tg_bot.token, parse_mode='HTML')
    dp = Dispatcher(bot=bot, storage=storage)
    dp.include_router(schedule.router)
    dp.include_router(activities.router)
    dp.include_router(scholarship.router)
    dp.include_router(faq.router)
    dp.include_router(feedback.router)
    dp.include_router(start.router)
    # dp.include_router(user.router)
    # dp.include_router(echo.router)
    # dp.include_router(admin.router)

    # start
    try:
        await dp.start_polling(bot)
    finally:
        await dp.storage.close()
        # await dp.storage.wait_closed()
        await bot.session.close()


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logger.error("Bot stopped!")
