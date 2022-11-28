import config
from aiogram import Bot, types, executor, Dispatcher

bot = Bot(token=config.token)
dp = Dispatcher(bot)

@dp.message_handler(commands=["start", "help"])
async def start(message: types.Message):
    await message.answer("Hi!")

@dp.message_handler(commands=["new_chat_members"])
async def start(message: types.Message):
    await message.answer("Добро пожаловать!")    