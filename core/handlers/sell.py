from aiogram import Router
from aiogram.types import Message

from aiogram.fsm.context import FSMContext


from core.keyboards.keyboard import confirm_keyboard
from core.lexicon.lexicon import SELL_USDT, TERMS_SELL, CONFIRM, CHOOSE_SELL
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


