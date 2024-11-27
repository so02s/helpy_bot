from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.scene import on

from handlers.change_room import CustomScene
from utils import obsidian as obs


'''
    Комната с заметками - можно создать заметку, она сохранится в определенный файл
'''

class NoteScene(CustomScene, state='note'):
    @on.message.enter()
    @on.callback_query.enter()
    async def on_msg_enter(self, message: Message = None) -> None:
        await message.answer('Комната с заметками')
    
    @on.message()
    async def process_message(self, msg: Message) -> None:
        note = obs.note_from_message(msg) # создание пустой заметки с датой
        # forward_info = get_forward_info(message) # если соо пересланное - получение того, кто переслал

        message_body = await obs.embed_formatting(msg) # это превращение в Markdown, если есть что
        note.text = message_body #  forward_info + # вся заметка (её текст)

        # if message.link_preview_options: # добавление ссылки на youtube, если есть
        #     if message.link_preview_options.url and 'youtu' in message.link_preview_options.url:
        #         note.text += f'\n![{message.link_preview_options.url}]({message.link_preview_options.url})\n'

        obs.save_message(note) # сохранение заметки

# router = Router()
# router.message.register(NoteScene.as_shandler(), Command('task'))

async def project(json_from_ai: str) -> None:
    note = obs.note_from_ai(json_from_ai)
    # TODO проверка насколько заполнен проект -> сохранить либо дописать
    # Возможно FSM 
    await obs.save_project(note)