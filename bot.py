import time
import logging

#import config

from aiogram import Bot, types, executor, Dispatcher

TOKEN = "5864815319:AAGLJHzbAUIVVHWCRu1rRDCGdBp3lE6NVXY"

MSG = "Мы давно не виделись!)"

bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot)

@dp.message_handler(commands=['start'])
async def start_hendler(message: types.Message):
    user_id = message.from_user.id
    user_name = message.from_user.full_name
    user_full_name = message.from_user.first_name
    logging.info(f'{user_id} {user_full_name} {time.asctime()}')   
    await message.reply(f'Привет, {user_full_name}!')

    for i in range(1):
        time.sleep(60)

        await bot.send_message(user_id, MSG.format(user_name))


#@dp.message_handler(commands=["new_chat_members"])
#async def start(message: types.Message):
    #await message.answer("Добро пожаловать!")    

    
if __name__ == '__main__':
    executor.start_polling(dp)