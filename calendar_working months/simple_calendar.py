import calendar
from datetime import datetime, timedelta

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.filters.callback_data import CallbackData
from aiogram.types import CallbackQuery
from aiogram3_calendar.calendar_types import SimpleCalendarCallback, SimpleCalendarAction, WEEKDAYS


class SimpleCalendar:

    @staticmethod
    async def start_calendar(
            year: int = datetime.now().year,
            month: int = datetime.now().month
    ) -> InlineKeyboardMarkup:
        """
        Creates an inline keyboard with the provided year and month
        :param int year: Year to use in the calendar, if None the current year is used.
        :param int month: Month to use in the calendar, if None the current month is used.
        :return: Returns InlineKeyboardMarkup object with the calendar.
        """

        markup = []
        ignore_callback = SimpleCalendarCallback(act=SimpleCalendarAction.IGNORE, year=year, month=month,
                                                 day=0)  # for buttons with no answer

        # First row - Month and Year
        markup.append(
            [
                InlineKeyboardButton(
                    text="<<",
                    callback_data=SimpleCalendarCallback(
                        act=SimpleCalendarAction.PREV_YEAR,
                        year=year, month=month,
                        day=1).pack()
                ),
                InlineKeyboardButton(
                    text=f'{calendar.month_name[month]} {str(year)}',
                    callback_data=ignore_callback.pack()
                ),
                InlineKeyboardButton(
                    text=">>",
                    callback_data=SimpleCalendarCallback(
                        act=SimpleCalendarAction.NEXT_YEAR,
                        year=year,
                        month=month,
                        day=1).pack()
                )
            ]
        )

        # Second row - Week Days
        markup.append(
            [InlineKeyboardButton(text=day, callback_data=ignore_callback.pack()) for day in WEEKDAYS]
        )

        # Calendar rows - Days of month
        month_calendar = calendar.monthcalendar(year, month)
        for week in month_calendar:
            calendar_row = []
            for day in week:
                if day == 0:
                    calendar_row.append(InlineKeyboardButton(text=" ", callback_data=ignore_callback.pack()))
                    continue
                calendar_row.append(InlineKeyboardButton(
                    text=str(day),
                    callback_data=SimpleCalendarCallback(act=SimpleCalendarAction.DAY, year=year, month=month, day=day).pack()
                ))
            markup.append(calendar_row)

        # Last row - Buttons
        markup.append(
            [
                InlineKeyboardButton(
                    text="<",
                    callback_data=SimpleCalendarCallback(
                        act=SimpleCalendarAction.PREV_MONTH,
                        year=year,
                        month=month,
                        day=day).pack()
                ),
                InlineKeyboardButton(
                    text=" ",
                    callback_data=ignore_callback.pack()),
                InlineKeyboardButton(
                    text=">",
                    callback_data=SimpleCalendarCallback(
                        act=SimpleCalendarAction.NEXT_MONTH,
                        year=year,
                        month=month,
                        day=day).pack()
                )
            ]
        )

        inline_kb = InlineKeyboardMarkup(inline_keyboard=markup, row_width=7)
        return inline_kb

    async def process_selection(self, query: CallbackQuery, data: [CallbackData, SimpleCalendarCallback]) -> tuple:
        """
        Process the callback_query. This method generates a new calendar if forward or
        backward is pressed. This method should be called inside a CallbackQueryHandler.
        :param query: callback_query, as provided by the CallbackQueryHandler
        :param data: callback_data, dictionary, set by calendar_callback
        :return: Returns a tuple (Boolean,datetime), indicating if a date is selected
                    and returning the date if so.
        """
        return_data = (False, None)
        temp_date = datetime(int(data.year), int(data.month), 1)
        print(temp_date)
        # processing empty buttons, answering with no action
        if data.act == SimpleCalendarAction.IGNORE:
            await query.answer(cache_time=60)
        # user picked a day button, return date
        if data.act == SimpleCalendarAction.DAY:
            await query.message.delete_reply_markup()  # removing inline keyboard
            return_data = True, datetime(int(data.year), int(data.month), int(data.day))
        # user navigates to previous year, editing message with new calendar
        if data.act == SimpleCalendarAction.PREV_YEAR:
            prev_date = datetime(int(data.year) - 1, int(data.month), 1)
            await query.message.edit_reply_markup(await self.start_calendar(int(prev_date.year), int(prev_date.month)))
        # user navigates to next year, editing message with new calendar
        if data.act == SimpleCalendarAction.NEXT_YEAR:
            next_date = datetime(int(data.year) + 1, int(data.month), 1)
            await query.message.edit_reply_markup(await self.start_calendar(int(next_date.year), int(next_date.month)))
        # user navigates to previous month, editing message with new calendar
        if data.act == SimpleCalendarAction.PREV_MONTH:
            prev_date = temp_date - timedelta(days=1)
            await query.message.edit_reply_markup(reply_markup=await self.start_calendar(int(prev_date.year), int(prev_date.month)))
        # user navigates to next month, editing message with new calendar
        if data.act == SimpleCalendarAction.NEXT_MONTH:
            next_date = temp_date + timedelta(days=31)
            print(next_date)
            await query.message.edit_reply_markup(reply_markup=await self.start_calendar(int(next_date.year), int(next_date.month)))
        # at some point user clicks DAY button, returning date
        return return_data
