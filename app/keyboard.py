from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,InlineKeyboardMarkup,InlineKeyboardButton)

main= ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='RGB MOD'),KeyboardButton(text='температура/влажность комнаты'),KeyboardButton(text='beep')],#later
    [KeyboardButton(text='Включить свет'),KeyboardButton(text='Выключить свет')],
],
resize_keyboard=True,
input_field_placeholder="выбери действие")

rgb= ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='red'),KeyboardButton(text='green'),KeyboardButton(text='blue')],
    [KeyboardButton(text='red 0'),KeyboardButton(text='green 0'),KeyboardButton(text='blue 0')],
    [KeyboardButton(text='ON ALL'),KeyboardButton(text='OFF ALL'),KeyboardButton(text='Exit')],
],
resize_keyboard=True,
input_field_placeholder="выбери действие")

settings=InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='test',url='https://google.com')]#test
])

