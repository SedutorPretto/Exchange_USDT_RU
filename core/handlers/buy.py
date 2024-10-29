from aiogram import Router
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from core.keyboards.keyboard import confirm_keyboard
from core.lexicon.lexicon import BUY_USDT, TERMS_BUY, CONFIRM, CHOOSE_BUY
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

