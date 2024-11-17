from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types.callback_query import CallbackQuery
from utils.filter import RoomCallbackFactory, room_now
from handlers.start import start_console

'''
    Этот хэндлер используется для перехода в разные "комнаты" -
    например, в комнату работы с заметками, тасками, ии и тд.
'''

router = Router()

# Выход из комнат
@router.message(Command("exit"))
async def exit_room(msg: Message):
    global room_now
    room_now = None
    start_console(msg)

# TODO Удаление сообщения с callback
@router.callback_query(RoomCallbackFactory)
async def change_room(callback: CallbackQuery, callback_data: RoomCallbackFactory):
    global room_now
    room_now = callback_data.room_name