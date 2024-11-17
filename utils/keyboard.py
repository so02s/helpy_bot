from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.types.callback_query import CallbackQuery
from utils.filter import RoomCallbackFactory

async def inline(callback: CallbackQuery, text: str, reply_markup):
    await callback.message.edit_text(text, reply_markup=reply_markup)

def testing():
    builder = InlineKeyboardBuilder()
    builder.button(text="Таска", callback_data=RoomCallbackFactory(room_name='task'))
    builder.button(text="Заметка", callback_data=RoomCallbackFactory(room_name='note'))
    builder.adjust(1)
    return builder.as_markup()