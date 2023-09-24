from aiogram import Dispatcher, Router, Bot, types, F
from aiogram.filters.command import Command
from aiogram.fsm.context import FSMContext
from aiogram.utils.markdown import hcode
from tgbot.keyboards.stars_kb.stars_from_main import schedule_stars_kb

from tgbot.database.database_stars import get_scholarship


router: Router = Router()


@router.message(F.text == "Когда стипендия 💸")
async def scholarship(message: types.Message, state: FSMContext):
    msg: str = get_scholarship()
    await message.answer(msg)
