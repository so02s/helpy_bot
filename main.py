import asyncio

from aiogram import Dispatcher
from aiogram.fsm.storage.memory import SimpleEventIsolation

from create_bot import bot

from handlers import add_statistic

async def start_bot():
    pass

async def stop_bot():
    pass

def create_dispatcher() -> Dispatcher:
    dispatcher = Dispatcher(
        events_isolation=SimpleEventIsolation(),
    )
    return dispatcher

async def main():
    dp = create_dispatcher()
    dp.include_routers(
        add_statistic.router
    )
    dp.startup.register(start_bot)
    dp.shutdown.register(stop_bot)

    try:
        await bot.delete_webhook(drop_pending_updates=True)
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == "__main__":
    asyncio.run(main())