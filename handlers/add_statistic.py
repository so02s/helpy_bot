from decouple import config
import datetime
from typing import Tuple

from aiogram import Router
from aiogram.filters import Command, CommandObject
from aiogram.types import Message

import httplib2
import apiclient
from oauth2client.service_account import ServiceAccountCredentials


CREDENTIALS_FILE = 'creds.json'
spreadsheet_id = config("SPREADSHEET_ID")

credentials = ServiceAccountCredentials.from_json_keyfile_name(
    CREDENTIALS_FILE,
    ['https://www.googleapis.com/auth/spreadsheets',
     'https://www.googleapis.com/auth/drive'])
httpAuth = credentials.authorize(httplib2.Http())
service = apiclient.discovery.build('sheets', 'v4', http = httpAuth)


def today_row_column() -> Tuple[str, int]:
    """
    Дает номер строки и столбца с нынешней датой
    """
    current_date = datetime.date.today()
    start_date = datetime.date(2025, 1, 29)

    diff = current_date - start_date

    column = chr(65 + (current_date.year - start_date.year) * 4)

    if(current_date.year != start_date.year):
        start_date = datetime.date(current_date.year, 1, 1)
        row = (current_date - start_date).days + 3
    else:
        row = diff.days + 3

    return column, row



router = Router()

@router.message(
    Command("новые")
)
async def add_new(msg: Message, command: CommandObject):

    args: str = command.args
    if not args:
        await msg.answer('Вы забыли добавить значение')
        return
    try:
        new_mans = int(args.split(' ')[0])
    except:
        await msg.answer('Непонятное количество')
        return

    column, row = today_row_column()
    column = chr(ord(column) + 2)

    values = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range=f"{column}{row}",
        majorDimension="ROWS"
    ).execute()

    new_values = int(values['values'][0][0]) + new_mans

    try:
        service.spreadsheets().values().batchUpdate(
            spreadsheetId=spreadsheet_id,
            body=
            {
                "valueInputOption": "USER_ENTERED",
                "data": [
                    {"range": f"{column}{row}",
                    "majorDimension": "ROWS",
                    "values": [[f"{new_values}"]]}
                ]
            }
        ).execute()
        await msg.answer(f'Добавлены, сегодня {new_values} новых людей')
    except:
        await msg.answer('Нет доступа к таблице')
    

@router.message(
    Command("старые")
)
async def add_new(msg: Message, command: CommandObject):

    args: str = command.args
    if not args:
        await msg.answer('Вы забыли добавить значение')
        return
    try:
        new_mans = int(args.split(' ')[0])
    except:
        await msg.answer('Непонятное количество')
        return

    column, row = today_row_column()
    column = chr(ord(column) + 1)

    values = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range=f"{column}{row}",
        majorDimension="ROWS"
    ).execute()

    new_values = int(values['values'][0][0]) + new_mans

    try:
        service.spreadsheets().values().batchUpdate(
            spreadsheetId=spreadsheet_id,
            body=
            {
                "valueInputOption": "USER_ENTERED",
                "data": [
                    {"range": f"{column}{row}",
                    "majorDimension": "ROWS",
                    "values": [[f"{new_values}"]]}
                ]
            }
        ).execute()
        await msg.answer(f'Добавлены, сегодня {new_values} новых людей')
    except:
        await msg.answer('Нет доступа к таблице')