from typing import Dict, List, Tuple, Union

from aiogram.types import CallbackGame, InlineKeyboardButton, InlineKeyboardMarkup, LoginUrl
from aiogram.utils.callback_data import CallbackData

from .base import BaseMarkupConstructor


class InlineMarkupConstructor(BaseMarkupConstructor):
    """
    Class for creating inline keyboards
    Usage example:
        class ExampleMarkup(InlineMarkupConstructor):
            callback_data = CallbackData('test', 'number')
            def get(self):
                schema = [3, 2, 1]
                actions = [
                    {'text': '1', 'callback_data': self.callback_data.new('1')},
                    {'text': '2', 'callback_data': self.callback_data.new('2')},
                    {'text': '3', 'callback_data': '3'},
                    {'text': '4', 'callback_data': self.callback_data.new('4')},
                    {'text': '5', 'callback_data': (self.callback_data, '5')},
                    {'text': '6', 'callback_data': '6'},
                ]
                return self.markup(actions, schema)
    """

    aliases = {"callback_data": ("cb", "cd", "callback", "data")}
    available_properties = [
        "text",
        "url",
        "login_url",
        "callback_data",
        "switch_inline_query",
        "switch_inline_query_current_chat",
        "callback_game",
        "pay",
    ]

    def _replace_aliases(
        self,
        action: Dict[
            str, Union[str, bool, Tuple[Dict[str, str], CallbackData], LoginUrl, CallbackGame]
        ],
    ):

        super(InlineMarkupConstructor, self)._replace_aliases(action)

    def _check_properties(
        self,
        action: Dict[
            str, Union[str, bool, Tuple[Dict[str, str], CallbackData], LoginUrl, CallbackGame]
        ],
    ) -> Dict[str, Union[str, bool, Tuple[Dict[str, str], CallbackData], LoginUrl, CallbackGame]]:
        return super(InlineMarkupConstructor, self)._check_properties(action)

    @staticmethod
    def _set_callback_data(
        button_data: Dict[
            str, Union[str, bool, Tuple[Dict[str, str], CallbackData], LoginUrl, CallbackGame]
        ],
    ):
        if isinstance(button_data["callback_data"], tuple):
            button_data["callback_data"] = button_data["callback_data"][0].new(
                button_data["callback_data"][1:]
            )
        elif not isinstance(button_data["callback_data"], str):
            raise ValueError(
                f'Invalid value for callback_data {type(button_data["callback_data"])} please use tuple, list or str'
            )

    def markup(
        self,
        actions: List[
            Dict[
                str, Union[str, bool, Tuple[Dict[str, str], CallbackData], LoginUrl, CallbackGame]
            ]
        ],
        schema: List[int],
    ) -> InlineKeyboardMarkup:
        markup = InlineKeyboardMarkup()
        markup.row_width = max(schema)
        buttons = list()
        for action in actions:
            self._replace_aliases(action)
            button_data = self._check_properties(action)

            if "callback_data" in button_data:
                self._set_callback_data(button_data)

            if "pay" in button_data:
                if len(buttons) != 0 and button_data["pay"]:
                    raise ValueError(
                        "pay type of button must always be the first button in the first row"
                    )
                button_data["pay"] = action["pay"]

            if len(button_data) != self.properties_amount:
                raise ValueError("Insufficient data to create a button")

            buttons.append(InlineKeyboardButton(**button_data))
        markup.inline_keyboard = self.create_keyboard_layout(buttons, schema)
        return markup