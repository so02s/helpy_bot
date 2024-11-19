from aiogram import Router, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.fsm.scene import Scene, SceneRegistry, ScenesManager, on
from aiogram.types.callback_query import CallbackQuery

from create_bot import bot
from utils import keyboard as kb

'''
    Это стартовая "пустая" комната. Отсюда открываются все остальные комнаты.
'''

# class MyScene(Scene, state="my_scene"):
#     @on.message.enter()
#     async def on_enter(self, message: Message):
#         await message.answer("Welcome to My Scene!")


router = Router()

@router.message(Command('exit'))
async def exit(message: Message, scene: ScenesManager = None):
    if scene:
        await scene.exit()
    await message.answer("Вы вышли из сцены.")

# @router.message(CommandStart())
# async def start_console(msg: Message, state: FSMContext = None):
#     await state.clear()
#     # await state.set_state(RoomStates.waiting_for_room)
#     msg_bot = await msg.answer(
#         'Приветик!\nТы молодец, продолжай в том же духе!',
#         reply_markup=kb.testing()
#     )
#     await bot.delete_messages(
#         msg.from_user.id,
#         [msg_bot.message_id - i for i in range(1, 10)]
#     )


# @router.callback_query(F.data == "start_model")
# async def start_cmd(callback: CallbackQuery, state: FSMContext):
#     await state.clear()
#     await kb.inline(
#         callback,
#         'Все получится, ты умничка',
#         reply_markup=kb.start_menu()
#     )