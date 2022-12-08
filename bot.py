import time
import logging

#import config

from aiogram import Bot, types, executor, Dispatcher

TOKEN = "5864815319:AAGLJHzbAUIVVHWCRu1rRDCGdBp3lE6NVXY"

bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot)

@dp.message_handler(commands=['start'])
def start_hendler(message: types.Message):
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name
    logging.INFO(f'{user_id} {user_full_name}', time.asctime()) 


#@dp.message_handler(commands=["new_chat_members"])
#async def start(message: types.Message):
    #await message.answer("Добро пожаловать!")    

    
