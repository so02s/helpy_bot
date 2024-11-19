import asyncio
from aiogram import Dispatcher

from create_bot import bot
from handlers import (
    start,
    task,
    # change_room,
    # note
)
from utils.filter import IsAdminMiddleware
from aiogram.fsm.scene import SceneRegistry
from aiogram.fsm.storage.memory import SimpleEventIsolation

async def start_bot():
    pass

async def stop_bot():
    pass

def create_dispatcher() -> Dispatcher:
    dispatcher = Dispatcher(
        events_isolation=SimpleEventIsolation(),
    )
    scene_registry = SceneRegistry(dispatcher)
    scene_registry.add(task.TaskScene)
    return dispatcher

async def main():
    dp = create_dispatcher()
    dp.include_routers(
        start.router,
    #     change_room.router,
        task.router,
    #     note.router
    )
    dp.startup.register(start_bot)
    dp.shutdown.register(stop_bot)
    dp.message.outer_middleware(IsAdminMiddleware())

    try:
        await bot.delete_webhook(drop_pending_updates=True)
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == "__main__":
    asyncio.run(main())