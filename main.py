import asyncio
from aiogram import Bot, Dispatcher, Router, types, F
from aiogram.filters import Command
from aiogram.types import Message, FSInputFile
import logging
import operator
import os
from dotenv import load_dotenv
from downloader import download_instagram_reel

load_dotenv()
API_TOKEN = os.getenv('API_TOKEN')
logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot=bot)
router = Router()
dp.include_router(router)


@router.message(F.text.contains("https://www.instagram.com/reel/") | F.text.contains("https://youtube.com/shorts/"))
async def send_reel(message: types.Message):
    try:
        file_name = download_instagram_reel(message.text)
        await message.reply_video(FSInputFile(file_name))
        os.remove(file_name)
    except Exception as e:
        await message.reply(f"Ошибка загрузки: {e}")
    
async def main():
    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()

if __name__ == '__main__':
    asyncio.run(main())
   