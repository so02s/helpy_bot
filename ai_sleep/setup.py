import logging

from decouple import config
from aiogram import Bot
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode


# логирование
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger=logging.getLogger(__name__)

# инициализация бота
bot = Bot(token=config('TOKEN_BOT'), default=DefaultBotProperties(parse_mode=ParseMode.HTML)) 
