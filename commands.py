from bot_config import dp, bot
from aiogram import types, Bot, Dispatcher, executor
import logging
import time

total = 150
# flag = 0  # флаг очередности

from random import randint
# from Keyboards.Standart import main_keyboard

# @dp.message_handler(commands=['start', 'help'])
# async def send_welcome(message: types.Message):
#     """
#     This handler will be called when user sends `/start` or `/help` command
#     """
#     await message.reply("Hi!\nI'm EchoBot!\nPowered by aiogram.")
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
    # flag = randint(0, 2)  # флаг очередности
    # if flag:
    #     await bot.send_message(message.chat.id, f"Первый ходит {player1}")
    # else:
    #     await bot.send_message(message.chat.id, f"Первый ходит бот")
  #
    # print (f'{message.from_user.first_name} взял {take}')
    # take = int(message.text)
    # if 0<take<29:
    #     total-=int(message.text)
    #     await message.reply(f'{message.from_user.first_name} взял {message.text} конфет  и осталось {total} конфет')
    # else:
    #     await  message.reply(f'Будь внимательнее. Возьми до 28 конфет')
    # k = randint(1, 29)
    # await bot.send_message(f"Бот взял {k} конфет")



# flag = randint(0, 2)  # флаг очередности
# if flag:
#     print(f"Первый ходит {player1}")
# else:
#     print(f"Первый ходит {player2}")
#
# counter1 = 0
# counter2 = 0
#

async def bot_calc(value):
    k = randint(1, 29)
    while value - k <= 28 and value > 29:
        k = randint(1, 29)
    return k

# def input_dat(name):
#     x = int()
#     while x < 1 or x > 28:
#         x = int(input(f"{name}, введите корректное количество конфет: "))
#     return x

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

    # player2 = 'Бот'
    # take = int(message.text)
    # if 0<take<29:
    #     total-=int(message.text)
    #     await message.reply(f'{message.from_user.first_name} взял {message.text} конфет  и осталось {total} конфет')
    # else:
    #     await  message.reply(f'Будь внимательнее. Возьми до 28 конфет')

    #
    # flag = randint(0, 2)  # флаг очередности
    # if flag:
    #     bot.send_message(message.chat.id, f"Первый ходит {player1}")
    # else:
    #     bot.send_message(message.chat.id, f"Первый ходит бот")
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

#
# if flag:
#     await bot.send_message(f"Выиграл {player1}")
# else:
#     await bot.send_message(f"Выиграл {player2}")

# @dp.message_handler(content_types=['text'])
# def handle_text(message):
#     bot.send_message(message.chat.id, bot_calc(message.text))

# from random import randint
#
# def input_dat(name):
#     x = int(input(f"{name}, введите количество конфет, которое возьмете от 1 до 28: "))
#     while x < 1 or x > 28:
#         x = int(input(f"{name}, введите корректное количество конфет: "))
#     return x
#
#
# def p_print(name, k, counter, value):
#     print(f"Ходил {name}, он взял {k}, теперь у него {counter}. Осталось на столе {value} конфет.")
#
#

#
# player1 = input("Введите имя первого игрока: ")
# player2 = "Bot"
# value = int(input("Введите количество конфет на столе: "))
# flag = randint(0, 2)  # флаг очередности
# if flag:
#     print(f"Первый ходит {player1}")
# else:
#     print(f"Первый ходит {player2}")
#
# counter1 = 0
# counter2 = 0
#
# while value > 28:
#     if flag:
#         k = input_dat(player1)
#         counter1 += k
#         value -= k
#         flag = False
#         p_print(player1, k, counter1, value)
#     else:
#         k = bot_calc(value)
#         counter2 += k
#         value -= k
#         flag = True
#         p_print(player2, k, counter2, value)
#
# if flag:
#     print(f"Выиграл {player1}")
# else:
#     print(f"Выиграл {player2}")
