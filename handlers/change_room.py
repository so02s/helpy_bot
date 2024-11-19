import sys
from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.scene import Scene, on, ScenesManager
from utils.filter import RoomCallbackFactory
from create_bot import bot
from utils import keyboard as kb

'''
    Переход по сценам
'''

class CustomScene(Scene):
    @on.message(Command('exit'))
    async def exit(self, msg: Message):
        await self.wizard.exit()
    
    @on.message.exit()
    async def on_exit(self, msg: Message) -> None:
        msg_bot = await msg.answer(
            'Приветик!\nТы молодец, продолжай в том же духе!',
            reply_markup=kb.testing()
        )
        await bot.delete_messages(
            msg.from_user.id,
            [msg_bot.message_id - i for i in range(1, 40)]
        )

router = Router()

@router.callback_query(RoomCallbackFactory.filter())
async def handle_room_callback(
    callback: CallbackQuery,
    callback_data: RoomCallbackFactory,
    scenes: ScenesManager # Заметка на будущее - ScenesManager ориентируется на state в дочке Scene
):
    await scenes.enter(callback_data.scene)
    # TODO удаление сообщений