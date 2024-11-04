from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.types.callback_query import CallbackQuery

async def inline(callback: CallbackQuery, text: str, reply_markup):
    await callback.message.edit_text(text, reply_markup=reply_markup)


def start_menu():
    buttons = [
        [   InlineKeyboardButton(text="Управление задачами и мероприятиями", callback_data="task_manager")],
        [   InlineKeyboardButton(text="Все мероприятия", callback_data="task_all")]
    ]
    kb = InlineKeyboardMarkup(inline_keyboard=buttons)
    return kb

def task_manager():
    buttons = [
        [   InlineKeyboardButton(text="Добавить", callback_data="add_task")],
        [   InlineKeyboardButton(text="Изменить", callback_data="change_task")],
        [   InlineKeyboardButton(text="Удалить", callback_data="del_task")],
        [   InlineKeyboardButton(text="Назад", callback_data="start_model")]
    ]
    kb = InlineKeyboardMarkup(inline_keyboard=buttons)
    return kb




# def reply_answers(cube_id: int, question_id: int, answers: list):
#     builder = InlineKeyboardBuilder()
#     for answer in answers:
#         builder.button(
#             text=f'{hex_to_emoji.get(answer.color, '')}   {answer.text}',
#             callback_data='UserCallbackFactory(cube_id=cube_id, answer_id=answer.id)'
#         )
#     builder.adjust(1)
#     return builder.as_markup()