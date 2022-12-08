import time
import logging

#import config

from aiogram import Bot, types, executor, Dispatcher

TOKEN = "5864815319:AAGLJHzbAUIVVHWCRu1rRDCGdBp3lE6NVXY"

bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot)

@dp.message_handler(commands=["start", "help"])
async def start(message: types.Message):
    await message.answer("Hi!")

@dp.message_handler(commands=["new_chat_members"])
async def start(message: types.Message):
    await message.answer("Добро пожаловать!")    

    
