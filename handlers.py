from aiogram import types, Dispatcher

import commands


def registred_handlers(dp: Dispatcher):
    dp.register_message_handler(commands.start_bot, commands=['start'])
    # dp.register_message_handler(commands.send_welcome, commands=['start'])
    dp.register_message_handler(commands.all_bot)
    # dp.register_message_handler(commands.game_bot)
    # dp.register_message_handler(commands.handle_text)