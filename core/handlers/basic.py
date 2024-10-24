from aiogram import Router, F, Bot
from aiogram.types import Message
from aiogram.filters import Command, CommandStart
from aiogram.fsm.context import FSMContext

from core.settings import settings
from core.keyboards.keyboard import main_keyboard
from core.lexicon.lexicon import WELCOME_TEXT, HELP


router = Router()


async def start_bot(bot: Bot):
    await bot.send_message(settings.tg_bot.admin_id, text='Бот завелся!')


async def stop_bot(bot: Bot):
    await bot.send_message(settings.tg_bot.admin_id, text='Бот заглох!')


@router.message(CommandStart())
async def send_welcome(message: Message, state: FSMContext):
    await state.clear()
    welcome_text = WELCOME_TEXT
    await message.answer(welcome_text, reply_markup=main_keyboard(), parse_mode="HTML")


@router.message(Command('cancel'))
@router.message(F.text.lower() == 'отмена')
async def action_cancel(message: Message, state: FSMContext):
    await state.clear()
    await state.set_data({})
    await message.answer(text='Действие отменено',
                         reply_markup=main_keyboard())


@router.message(Command('help'))
async def helper(message: Message):
    await message.answer(text=HELP,
                         reply_markup=main_keyboard())



