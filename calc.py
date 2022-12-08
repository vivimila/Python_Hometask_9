# Создайте калькулятор.


import os
import sys
import random


from telegram import InlineKeyboardButton, InlineKeyboardMarkup, User
from telegram.ext import Updater, CommandHandler, MessageHandler, \
    ConversationHandler, Filters, CallbackQueryHandler

import strings as st



def start(update, context):
    context.bot.send_message(
        update.effective_chat.id,
        f"Привет! Я бот-калькулятор\n"
        f"/calc - сделать расчет\n"
        f"/convert - перевести доллары в рубли")


def calc(update, context):
    context.bot.send_message(
        update.effective_chat.id,
        f"Введите выражение\n Для выхода нажмите /stop")
    return 1


def eval_calc(update, context):
    context.bot.send_message(
        update.effective_chat.id,
        f"Результат: {eval(update.message.text)}")


def convert(update, context):
    context.bot.send_message(
        update.effective_chat.id,
        f"Введите сумму в $\n Для выхода нажмите /stop")
    return 1


def converter(update, context):
    context.bot.send_message(
        update.effective_chat.id,
        f"Результат: {int(update.message.text) * 55.3}")


def stop(update, context):
    return update.message.reply_text(st.ANSW_STOP), ConversationHandler.END


calc_handler = ConversationHandler(
    entry_points=[CommandHandler('calc', calc)],
    states={
        1: [MessageHandler(Filters.text & ~Filters.command, eval_calc)],
    },
    fallbacks=[CommandHandler('stop', stop)]
)
convert_handler = ConversationHandler(
    entry_points=[CommandHandler('convert', convert)],
    states={
        1: [MessageHandler(Filters.text & ~Filters.command, converter)],
    },
    fallbacks=[CommandHandler('stop', stop)]
)

start_handler = CommandHandler('start', start)