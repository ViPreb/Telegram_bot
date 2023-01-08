from bot_config import dp
# from aiogram import executor, types
# import logging
#
# logging.basicConfig(level=logging.INFO)
#
#
async def bot_start(_):
    print("Бот запущен")
#
#
#
# if __name__ == '__main__':
#     executor.start_polling(dp, on_startup = bot_start, skip_updates=True)
#
# @dp.message_handler(commands=['start', 'help'])
# async def send_welcome(message: types.Message):
#     """
#     This handler will be called when user sends `/start` or `/help` command
#     """
#     await message.reply("Hi!\nI'm EchoBot!\nPowered by aiogram.")

import logging

from aiogram import executor, types
import handlers


# # Configure logging
# logging.basicConfig(level=logging.INFO)


handlers.registred_handlers(dp)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup = bot_start)