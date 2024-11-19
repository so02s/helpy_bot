from aiogram import Router, F
from aiogram.filters import Command, StateFilter
from aiogram.types import Message
from aiogram.types.callback_query import CallbackQuery
from aiogram.fsm.scene import Scene, on
from utils.filter import RoomCallbackFactory
from utils.globals import Globals
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

'''
    Это класс, от которого наследуются все сцены в проекте
'''

class CustomScene(Scene):
    @on.message(F.text == 'выйти')
    async def exit(self, msg: Message):
        await self.wizard.exit()
        await bot.delete_messages(
            msg.from_user.id,
            [msg_bot.message_id - i for i in range(1, 100)]
        )
    
    @on.message.exit()
    async def on_exit(self, msg: Message) -> None:
        await message.answer('Вышли из тасков')


# router = Router()

# А теперь пробуем через scenes wizard

# class RoomStates(StatesGroup):
#     waiting_for_room = State()
#     in_room = State()

# @router.message(Command("exit"), StateFilter('*'))
# async def exit_room(msg: Message, state: FSMContext):
#     await state.finish()

# @router.callback_query(RoomCallbackFactory.filter(), StateFilter('*'))
# async def change_room(callback: CallbackQuery, callback_data: RoomCallbackFactory, state: FSMContext):
#     await state.update_data(room_name=callback_data.room_name)
#     await callback.answer(f"Теперь вы в комнате {callback_data.room_name}")


# Попытка с middleware

# Выход из комнат
# @router.message(Command("exit"))
# async def exit_room(msg: Message):
#     Globals().room_now = None
#     await start_console(msg)

# # TODO Удаление сообщения с callback
# @router.callback_query(RoomCallbackFactory.filter())
# async def change_room(callback: CallbackQuery, callback_data: RoomCallbackFactory):
#     Globals().room_now = callback_data.room_name
#     await callback.answer(f"теперь вы в комнате {callback_data.room_name}")