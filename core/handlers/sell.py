from aiogram import Router, F, Bot
from aiogram.types import Message, ReplyKeyboardRemove

from aiogram.fsm.context import FSMContext

from core.settings import settings
from core.keyboards.keyboard import confirm_keyboard
from core.lexicon.lexicon import SELL_USDT, TERMS_SELL, CONFIRM, CHOOSE_SELL, CONFIRM_FOR_USER, CHOOSE_SELL_AGAIN, CHOOSE_SELL_MORE
from core.handlers.states import FSMDealSell

router = Router()


@router.message(lambda message: message.text == SELL_USDT)
async def terms_trade_option(message: Message, state: FSMContext):
    await state.set_state(FSMDealSell.choosing_sell)
    await message.answer(TERMS_SELL, reply_markup=confirm_keyboard(), parse_mode="HTML")


@router.message(FSMDealSell.choosing_sell, lambda message: message.text == CONFIRM)
async def process_trade(message: Message, state: FSMContext):
    await state.clear()
    await message.answer(CHOOSE_SELL)


@router.message(FSMDealSell.choosing_sell_confirm, lambda message: message.text.isdigit() and int(message.text) < 100)
async def wrong_quantity(message: Message):
    await message.answer(CHOOSE_SELL_MORE, parse_mode="HTML")


@router.message(lambda message: message.text.isdigit(), FSMDealSell.choosing_sell_confirm)
async def process_amount(message: Message, state: FSMContext):
    await state.set_state(FSMDealSell.choosing_sell_finish)
    amount = message.text
    confirmation_text = f"Вы хотите продать {amount} USDT?"
    await state.update_data(amount=amount)
    await message.answer(confirmation_text, reply_markup=confirm_keyboard())


@router.message(FSMDealSell.choosing_sell_confirm)
async def wrong_digits(message: Message):
    await message.answer(CHOOSE_SELL_AGAIN, parse_mode="HTML")


@router.message(FSMDealSell.choosing_sell_finish, lambda message: message.text == CONFIRM)
async def process_finish(message: Message, state: FSMContext, bot: Bot):
    await message.answer(CONFIRM_FOR_USER, reply_markup=ReplyKeyboardRemove())
    user_data = await state.get_data()
    specialist_chat_id = settings.tg_bot.seller_id
    user_info = f'Пользователь @{message.from_user.username} хочет продать {user_data["amount"]} USDT.'
    await bot.send_message(specialist_chat_id, user_info)
