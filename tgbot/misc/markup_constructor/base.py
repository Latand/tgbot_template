from abc import ABC, abstractmethod
from typing import List, Union

from aiogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    KeyboardButton,
    ReplyKeyboardMarkup,
)


class BaseMarkupConstructor(ABC):
    aliases = {}
    available_properties = []
    properties_amount = 2

    def __init__(self):
        if not self.aliases:
            raise ValueError("You need to specify aliases")
        if not self.available_properties:
            raise ValueError("You need to specify available_properties")
        if self.properties_amount < self.properties_amount:
            raise ValueError(f"properties_amount can't be less then {self.properties_amount}")

    def _replace_aliases(
            self,
            action,
    ):
        for value, aliases in self.aliases.items():
            if isinstance(aliases, tuple) or isinstance(aliases, list):
                for alias in aliases:
                    if alias in action:
                        action[value] = action.pop(alias)
            elif isinstance(aliases, str):
                if aliases in action:
                    action[value] = action.pop(aliases)
            else:
                raise ValueError(
                    f"Invalid datatype for alias {type(aliases)} please use tuple, list or str"
                )

    def _check_properties(
            self,
            action,
    ):
        button_data = dict()
        for key in action:
            if key in self.available_properties:
                if len(button_data) < self.properties_amount:
                    button_data[key] = action[key]
                else:
                    raise ValueError(
                        f"You must use exactly one of the optional fields."
                        f"Received {len(button_data)} expected {self.properties_amount}"
                    )
            else:
                raise ValueError(f"Invalid value {key} please use {self.available_properties} ")
        return button_data

    @staticmethod
    def create_keyboard_layout(
            buttons: List[Union[InlineKeyboardButton, KeyboardButton]], scheme: List[int]
    ) -> List[List[Union[InlineKeyboardMarkup, ReplyKeyboardMarkup]]]:
        if sum(scheme) != len(buttons):
            raise ValueError("The number of buttons does not match the scheme")
        keyboard = []
        for row in scheme:
            keyboard.append([])
            for _ in range(row):
                keyboard[-1].append(buttons.pop(0))
        return keyboard

    @abstractmethod
    def markup(self, actions, schema):
        pass
