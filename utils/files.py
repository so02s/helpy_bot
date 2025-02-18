import aiofiles
from pathlib import Path

async def read_file(filepath: Path) -> str:
    async with aiofiles.open(filepath, mode='r') as file:
        content = await file.read()
        return content