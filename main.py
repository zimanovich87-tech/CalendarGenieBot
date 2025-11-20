import asyncio
import os
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

# Настройка логирования
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Получаем токен из переменных окружения
BOT_TOKEN = os.getenv('BOT_TOKEN')
if not BOT_TOKEN:
    logger.error("❌ BOT_TOKEN не найден!")
    exit(1)

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("🧞‍♂️ Calendar Genie Bot работает на Render!")

@dp.message()
async def echo(message: types.Message):
    await message.answer("✅ Бот активен! Используйте /start")

async def main():
    logger.info("🚀 Бот запускается на Render...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
