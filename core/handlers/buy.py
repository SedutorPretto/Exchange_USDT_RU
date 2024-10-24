from aiogram import Router, F, Bot
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.fsm.context import FSMContext

from core.settings import settings
from core.keyboards.keyboard import confirm_keyboard
from core.lexicon.lexicon import BUY_USDT, TERMS_BUY, CONFIRM, CHOOSE_BUY, CONFIRM_FOR_USER, CHOOSE_BUY_AGAIN, CHOOSE_BUY_MORE
from core.handlers.states import FSMDealBuy

router = Router()


@router.message(lambda message: message.text == BUY_USDT)
async def terms_trade_option(message: Message, state: FSMContext):
    await state.set_state(FSMDealBuy.choosing_buy_terms)
    await message.answer(TERMS_BUY, reply_markup=confirm_keyboard(), parse_mode="HTML")


@router.message(FSMDealBuy.choosing_buy_terms, lambda message: message.text == CONFIRM)
async def process_trade(message: Message, state: FSMContext):
    await state.set_state(FSMDealBuy.choosing_buy_confirm)
    await message.answer(CHOOSE_BUY)


@router.message(FSMDealBuy.choosing_buy_confirm, lambda message: message.text.isdigit() and int(message.text) < 50)
async def wrong_quantity(message: Message):
    await message.answer(CHOOSE_BUY_MORE, parse_mode="HTML")


@router.message(lambda message: message.text.isdigit(), FSMDealBuy.choosing_buy_confirm)
async def process_amount(message: Message, state: FSMContext):
    await state.set_state(FSMDealBuy.choosing_buy_finish)
    amount = message.text
    confirmation_text = f"Вы хотите купить {amount} USDT?"
    await state.update_data(amount=amount)
    await message.answer(confirmation_text, reply_markup=confirm_keyboard())


@router.message(FSMDealBuy.choosing_buy_confirm)
async def wrong_digits(message: Message):
    await message.answer(CHOOSE_BUY_AGAIN, parse_mode="HTML")


@router.message(FSMDealBuy.choosing_buy_finish, lambda message: message.text == CONFIRM)
async def process_finish(message: Message, state: FSMContext, bot: Bot):
    await message.answer(CONFIRM_FOR_USER, reply_markup=ReplyKeyboardRemove())
    user_data = await state.get_data()
    specialist_chat_id = settings.tg_bot.seller_id
    user_info = f'Пользователь @{message.from_user.username} хочет купить {user_data["amount"]} USDT.'
    await bot.send_message(specialist_chat_id, user_info)
