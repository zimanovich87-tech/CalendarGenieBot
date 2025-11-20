import asyncio
import os
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

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

# Клавиатура главного меню
def get_main_menu():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="📅 Мои события"), KeyboardButton(text="🎯 Создать слот")],
            [KeyboardButton(text="⚙️ Настройки"), KeyboardButton(text="❓ Помощь")]
        ],
        resize_keyboard=True,
        input_field_placeholder="Выберите действие..."
    )

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer(
        "🧞‍♂️ Добро пожаловать в Calendar Genie Bot!\n\n"
        "Выберите действие в меню ниже:",
        reply_markup=get_main_menu()
    )

@dp.message(Command("menu"))
async def cmd_menu(message: types.Message):
    await message.answer(
        "📋 Главное меню:",
        reply_markup=get_main_menu()
    )

@dp.message(lambda message: message.text == "📅 Мои события")
async def show_events(message: types.Message):
    await message.answer("📅 Раздел 'Мои события' в разработке...")

@dp.message(lambda message: message.text == "🎯 Создать слот")
async def create_slot(message: types.Message):
    await message.answer("🎯 Раздел 'Создать слот' в разработке...")

@dp.message(lambda message: message.text == "⚙️ Настройки")
async def show_settings(message: types.Message):
    await message.answer("⚙️ Раздел 'Настройки' в разработке...")

@dp.message(lambda message: message.text == "❓ Помощь")
async def show_help(message: types.Message):
    help_text = """
🤖 Помощь по Calendar Genie:

📅 Мои события - просмотр ваших задач и встреч
🎯 Создать слот - создать временные слоты для бронирования  
⚙️ Настройки - настройки календаря и уведомлений

Используйте /menu чтобы открыть меню кнопок
"""
    await message.answer(help_text)

@dp.message()
async def echo(message: types.Message):
    await message.answer(
        "Используйте меню или команды:\n/start - начать\n/menu - показать меню\n/help - помощь",
        reply_markup=get_main_menu()
    )

async def main():
    logger.info("🚀 Бот с кнопочным меню запускается...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
