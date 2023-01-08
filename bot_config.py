from aiogram import Bot, Dispatcher
import logging
# from aiogram.dispatcher import Dispatcher

API_TOKEN = '5811158002:AAE7oveIl034egZvWiQTVEEI7If7_wfaxVs'

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# logging.basicConfig(level=logging.INFO)