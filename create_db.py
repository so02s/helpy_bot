import asyncio

from db.models import create_all_tables

asyncio.run(create_all_tables())