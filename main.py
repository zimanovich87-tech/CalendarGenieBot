import asyncio
import os
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiohttp import web

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
        resize_keyboard=True
    )

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer(
        "🧞‍♂️ Добро пожаловать в Calendar Genie Bot!\n\n"
        "Выберите действие в меню ниже:",
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
    await message.answer(
        "🤖 Помощь по боту:\n\n"
        "📅 Мои события - просмотр ваших задач\n"
        "🎯 Создать слот - создать временные слоты\n"
        "⚙️ Настройки - настройки бота\n\n"
        "Бот работает на Render.com 🚀"
    )

# HTTP сервер для здоровья (для Render)
async def health_check(request):
    return web.Response(text="Calendar Genie Bot is running!")

async def start_bot():
    logger.info("🚀 Бот запускается на Render...")
    await dp.start_polling(bot)

async def start_http():
    app = web.Application()
    app.router.add_get('/', health_check)
    app.router.add_get('/health', health_check)
    
    runner = web.AppRunner(app)
    await runner.setup()
    
    site = web.TCPSite(runner, '0.0.0.0', int(os.getenv('PORT', 10000)))
    await site.start()
    logger.info("🌐 HTTP сервер запущен")

async def main():
    await asyncio.gather(
        start_bot(),
        start_http()
    )

if __name__ == "__main__":
    asyncio.run(main())
