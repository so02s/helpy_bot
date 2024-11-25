import os
import json
from datetime import datetime as dt
from pytz import timezone
from aiogram.types import Message, MessageEntity

import aiofiles

# мне не нравится, что сохраняется по времени 
# TODO переделать под заголовки
class Note:
    def __init__(
        self,
        name = "",
        text = "",
        path = "",
        date = dt.now().strftime('%Y-%m-%d'),
        time = dt.now().strftime('%H:%M:%S'),
        from_usr = "",
        tags = None,
        files = None,
        links = None,
        
        # Дальше для проектов
        goal = None
    ):
        self.text = text
        self.date = date
        self.time = time
        self.path = path
        self.from_usr = from_usr
        self.tags = tags
        self.files = files
        self.links = links
        
        self.goal = goal


def note_from_ai(text: str) -> Note:
    data = json.loads(text)
    
    name = data.get("name", "Без названия")
    project_text = data.get("text", "Описание отсутствует")
    goal = data.get("goals", [])
    files = data.get("files", [])
    links = data.get("links", [])
    tags = data.get("tags", [])
    
    note = Note(
        name=name,
        text=project_text,
        goal=goal,
        files=files,
        links=links,
        tags=tags
    )
    
    return note


def get_note_name(curr_date) -> str:
    date_parts = curr_date.split('-')
    year, month, day = date_parts[0], date_parts[1], date_parts[2]
    
    note_name = 'Telegram-{year}-{month}-{day}'.format(year=year, month=month, day=day)
    return os.path.join(r"E:\spheres_of_life\DeepSleep", f'{note_name}.md')

# TODO перевести на ассинхронное выполнение + сохранение в определенный файл
async def save_message(note: Note) -> None:
    
    curr_date = note.date
    curr_time = note.time
    note_text = f'#### [[{curr_date}]] {curr_time}\n{note.text}\n\n'
    
    with open(get_note_name(curr_date), 'a', encoding='UTF-8') as f:
        f.write(note_text)
        
async def save_project(note: Note) -> None:
    # TODO шаблон для проектов
    
    # TODO тут еще настройку из файла (путь до основной папки)
    # типо этого r"E:\spheres_of_life\DeepSleep"
    with aiofiles.open("E:\spheres_of_life\\testing_void\Projects\\" + note.path, 'a', encoding='UTF-8') as f:
        await f.write(note_text)



def note_from_message(message: Message):
    local_tz = timezone('Europe/Moscow')
    message_date = message.date.astimezone(local_tz)
    msg_date = message_date.strftime('%Y-%m-%d')
    msg_time = message_date.strftime('%H:%M:%S')
    note = Note(date=msg_date, time=msg_time)
    return note

def to_u16(text: str) -> bytes:
    return text.encode('utf-16-le')

formats = {'bold': ('**', '**'),
           'italic': ('_', '_'),
           'underline': ('<u>', '</u>'),
           'strikethrough': ('~~', '~~'),
           'code': ('`', '`'),
           'spoiler': ('==', '=='),
}

def parse_entities(text: bytes,
    entities: list[MessageEntity],
    offset: int,
    end: int) -> str:
    formatted_note = ''

    for entity_index, entity in enumerate(entities):
        entity_start = entity.offset * 2
        if entity_start < offset:
            continue
        if entity_start > offset:
            formatted_note += from_u16(text[offset:entity_start])
        offset = entity_end = entity_start + entity.length * 2

        format = entity.type
        if format == 'pre':
            pre_content = from_u16(text[entity_start:entity_end])
            content_parts = partition_string(pre_content)
            formatted_note += '```'
            if (len(content_parts[0]) == 0 and
                content_parts[1].find('\n') == -1):
                formatted_note += '\n'
            formatted_note += pre_content
            if content_parts[2].find('\n') == -1:
                formatted_note += '\n'
            formatted_note += '```'
            if (len(text) - entity_end < 2 or
               from_u16(text[entity_end:entity_end+2])[0] != '\n'):
                formatted_note += '\n'
            continue
        # parse nested entities for example: "**bold _italic_**"
        sub_entities = [e for e in entities[entity_index + 1:] if e.offset * 2 < entity_end]
        parsed_entity = parse_entities(text, sub_entities, entity_start, entity_end)
        content_parts = partition_string(parsed_entity)
        content = content_parts[1]
        if format in formats:
            format_code = formats[format]
            formatted_note += content_parts[0]
            i = 0
            while i < len(content):
                index = content.find('\n\n', i) # inline formatting across paragraphs, need to split
                if index == -1:
                    formatted_note += format_code[0] + content[i:] + format_code[1]
                    break
                formatted_note += format_code[0] + content[i:index] + format_code[1]
                i = index
                while i < len(content) and content[i] == '\n':
                    formatted_note += '\n'
                    i += 1
            formatted_note += content_parts[2]
            continue
        if format == 'mention':
            formatted_note += f'{content_parts[0]}[{content}](https://t.me/{content[1:]}){content_parts[2]}'
            continue
        if format == 'text_link':
            formatted_note += f'{content_parts[0]}[{content}]({entity.url}){content_parts[2]}'
            continue
        # Not processed (makes no sense): url, hashtag, cashtag, bot_command, email, phone_number
        # Not processed (hard to visualize using Markdown): spoiler, text_mention, custom_emoji
        formatted_note += parsed_entity

    if offset < end:
        formatted_note += from_u16(text[offset:end])
    return formatted_note

def is_single_url(message: Message) -> bool:
    # assuming there is atleast one entity
    entities = message.entities
    url_entity = entities[0]
    if url_entity.type == "url":
        return True
    if url_entity.type != "text_link":
        return False
    # need to check nested entities
    url_end = url_entity.offset + url_entity.length
    for e in entities[1:]:
        if e.offset > url_end:
            return False
    return True


async def get_url_info_formatting(url: str) -> str:
    async with aiohttp.ClientSession() as session:
        page = await download(url, session)
        og_props = get_open_graph_props(page)
        if 'image' in og_props or 'description' in og_props:
            sep = ''
            image = ''
            callout_type = "[!link-info-ni]"
            if 'image' in og_props:
                image += "!["
                if 'image:alt' in og_props:
                   image += og_props['image:alt'].replace("\n", " ")
                image += f"]({og_props['image']})"
                if 'image:width' in og_props and int(og_props['image:width']) < 600:
                    callout_type = "[!link-info]"
                else:
                    callout_type = "[!link-preview]"
                sep = "\n>"
            formatted_note = f'\n> {callout_type}'
            if 'site_name' in og_props:
                formatted_note += f" [{og_props['site_name']}]({url})"
            if 'title' in og_props:
                formatted_note += "\n> # " + og_props['title']
            if 'description' in og_props:
                formatted_note += "\n> "
                formatted_note += "\n> ".join(og_props['description'].split('\n')) + sep
            if 'image' in og_props:
                formatted_note += f"\n> [{image}]({url})"
            return formatted_note + "\n"
        return ''


async def embed_formatting(message: Message) -> str:
    note = message.text or ""

    if not message.entities or len(message.entities) == 0:
        return note

    entities = message.entities
    formatted_note = ''
    try:
        note_u16 = to_u16(note)
        formatted_note = parse_entities(note_u16, entities, 0, len(note_u16))
        if is_single_url(message):
            url_entity = entities[0]
            url = url_entity.get_text(note) if url_entity['type'] == "url" else url_entity['url']
            formatted_note += await get_url_info_formatting(url)
    except Exception as e:
        # If the message does not contain any formatting
        # await message.reply(f'🤷‍♂️ {e}')
        formatted_note = note
    return formatted_note


# ================= Шаблоны

# Проекты
def get_project_text(note: Note) -> str:
    goals_list = "\n".join(f"- [ ] {goal}" for goal in note.goal)
    files_list = "\n".join(f"- [[{file}]]" for file in note.files)
    links_list = "\n".join(f"- [{link['name']}]({link['url']})" for link in note.links)

    project_text = f"""# Проект: {note.name}

## Описание
{note.text}

## Задачи
{goals_list}

## Ссылки на другие файлы
{files_list}

## Внешние ресурсы
{links_list}

## Теги
{' '.join(f'[[{tag}]]' for tag in note.tags)}
"""

    return project_text