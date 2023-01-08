from bot_config import dp, bot
from aiogram import types, Bot, Dispatcher, executor
import logging
import time

total = 150


from random import randint

@dp.message_handler(commands=['start'])
async def start_bot(message: types.Message):
    # print(message)
    global player1
    user_id = message.from_user.id
    player1 = message.from_user.first_name
    # user_full_name = message.from_user.full_name
    # logging.info(f'{user_id} {player1} {time.asctime()}')
    await message.answer(f"Привет, {player1}! Поиграем в конфеты с ботом. Выберем, кто ходит первый?\n"
                         f"да/нет")
 
async def bot_calc(value):
    k = randint(1, 29)
    while value - k <= 28 and value > 29:
        k = randint(1, 29)
    return k


@dp.message_handler(text=['да'])
async def all_bot(message: types.Message):
    # print(message)
    # print(message.text)
    # await bot.send_message(message.from_user.id, f'{message.from_user.first_name}, да что ты говоришь?!')
    # await message.reply(f'{message.from_user.first_name}, да что ты говоришь?!')
    global total
    # global flag
    player1 = message.from_user.first_name
    flag = randint(0, 2)  # флаг очередности
    if flag:
        await bot.send_message(message.chat.id, f"Первый ходит {player1}")
    else:
        await bot.send_message(message.chat.id, f"Первый ходит бот")

# @dp.message_handler()
# async def game_bot(message: types.Message):
    counter1 = 0
    counter2 = 0
    # global flag
    while total > 28:
        if flag:
            await bot.send_message(message.from_user.id, f"Введи корректное количество конфет от 1 до 28")
            k = int(message.text)
            if 0 < k < 29:
                counter1 += k
                total -=k
                await message.reply(f'{message.from_user.first_name} взял {k} конфет, теперь у него {counter1}  и осталось {total} конфет')
            else:
                await message.answer(f'Будь внимательнее. Возьми до 28 конфет')
            flag = False
        else:
            k = await bot_calc(total)
            counter2 += k
            total -= k
            await bot.send_message(message.chat.id, f'Бот взял {k} конфет, теперь у него {counter2}  и осталось {total} конфет')
            flag = True
    if flag:
        await bot.send_message(message.chat.id, f"Выиграл {player1}")
    else:
        await bot.send_message(message.chat.id, f"Выиграл бот")


