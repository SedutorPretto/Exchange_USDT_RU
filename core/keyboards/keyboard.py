from aiogram.utils.keyboard import ReplyKeyboardBuilder, ReplyKeyboardMarkup, KeyboardButton
from core.lexicon.lexicon import BUY_USDT, SELL_USDT, CONFIRM, CANCEL


def main_keyboard() -> ReplyKeyboardMarkup:
    builder = ReplyKeyboardBuilder()
    builder.add(KeyboardButton(text=BUY_USDT), KeyboardButton(text=SELL_USDT))
    builder.adjust(2)
    return builder.as_markup(resize_keyboard=True, one_time_keyboard=True)


def confirm_keyboard() -> ReplyKeyboardMarkup:
    builder = ReplyKeyboardBuilder()
    builder.add(KeyboardButton(text=CONFIRM), KeyboardButton(text=CANCEL))
    builder.adjust(2)
    return builder.as_markup(resize_keyboard=True, one_time_keyboard=True)
