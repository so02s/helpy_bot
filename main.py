import asyncio

from aiogram import Dispatcher
from aiogram.fsm.storage.memory import SimpleEventIsolation

from ai_sleep.setup import bot
from handlers import (
    start,
    ai
)
from utils.filter import IsAdminMiddleware


def create_dispatcher() -> Dispatcher:
    dispatcher = Dispatcher(
        events_isolation=SimpleEventIsolation(),
    )
    return dispatcher

async def main():
    dp = create_dispatcher()
    dp.include_routers(
        start.router,
        ai.router,
    )
    dp.message.outer_middleware(IsAdminMiddleware())

    try:
        await bot.delete_webhook(drop_pending_updates=True)
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


# TODO в 23 запуск "сна" - и в 7:00 выключение сна

if __name__ == "__main__":
    asyncio.run(main())