import sys
import asyncio
import logging


from aiogram import Bot, Dispatcher

from core.settings import settings
from core.handlers import basic, buy, sell

from core.keyboards.set_menu import set_common_menu


async def start():
    bot = Bot(token=settings.tg_bot.bot_token)
    dp = Dispatcher()

    await set_common_menu(bot)

    dp.include_router(basic.router)
    dp.include_router(buy.router)
    dp.include_router(sell.router)
    dp.startup.register(basic.start_bot)
    dp.shutdown.register(basic.stop_bot)

    await bot.delete_webhook(drop_pending_updates=True)
    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == '__main__':
    logging.basicConfig(level=logging.WARNING, stream=sys.stdout)
    asyncio.run(start())
