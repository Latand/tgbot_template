from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup


class Schedule(StatesGroup):
    type = State()


class Activities(StatesGroup):
    type = State()


class Faq(StatesGroup):
    type = State()


class Feedback(StatesGroup):
    send = State()
