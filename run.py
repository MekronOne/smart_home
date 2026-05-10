import asyncio
import logging

import app.arduino as arduino_mod 
from app.arduino import connect
from aiogram import Bot,Dispatcher,F
from aiogram.filters import CommandStart,Command
from aiogram.types import Message
import app.keyboard as kb
from config import TOKEN

bot=Bot(token=TOKEN)
dp=Dispatcher()

@dp.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer('привет!!!\nэтот бот используется для управления умным домом\n',
                         reply_markup=kb.main)#hi massage

@dp.message(F.text == "RGB MOD")                    #TODO:добавить выход из мода ргб ГОТОВО!!
async def helpGet(message: Message):
    await message.answer('RGB MOD ON!!!',
                         reply_markup=kb.rgb)
    
@dp.message(F.text == "Exit")                      #TODO:добавить выход из мода ргб ГОТОВО!!
async def helpGet(message: Message):
    await message.answer('RGB MOD OFF!!!',
                         reply_markup=kb.main)

@dp.message(F.text == "Включить свет")  
async def cmd_on_text(message: Message):                        #TODO: убрать отладочную шнягу со всех команд бота!!!!
    if arduino_mod.arduino and arduino_mod.arduino.is_open:
        try:
            arduino_mod.write(b'1')
            await message.answer("LED ON")
        except Exception as e:
            await message.answer(f"err: {e}")
    else:
        await message.answer("no conection")

@dp.message(F.text == "Выключить свет")                 #TODO: добавить такую функцию для rgb led #ГОТОВО
async def cmd_off_text(message: Message):
    if arduino_mod.arduino and arduino_mod.arduino.is_open:
        try:
            arduino_mod.write(b'0')
            await message.answer("LED OFF")
        except Exception as e:
            await message.answer(f"err: {e}")
    else:
        await message.answer("no conection")

@dp.message(F.text == "red")                    #RGB ON
async def cmd_on_text(message: Message):
    if arduino_mod.arduino and arduino_mod.arduino.is_open:
        try:
            arduino_mod.write(b'r')
            await message.answer("red LED ON")
        except Exception as e:
            await message.answer(f"err: {e}")
    else:
        await message.answer("no conection")

@dp.message(F.text == "green")  
async def cmd_on_text(message: Message):
    if arduino_mod.arduino and arduino_mod.arduino.is_open:
        try:
            arduino_mod.write(b'g')
            await message.answer("green LED ON")
        except Exception as e:
            await message.answer(f"err: {e}")
    else:
        await message.answer("no conection")

@dp.message(F.text == "blue")  
async def cmd_on_text(message: Message):
    if arduino_mod.arduino and arduino_mod.arduino.is_open:
        try:
            arduino_mod.write(b'b')
            await message.answer("blue LED ON")
        except Exception as e:
            await message.answer(f"err: {e}")
    else:
        await message.answer("no conection")         #RGB ON



@dp.message(F.text == "red 0")                      #RGB OFF
async def cmd_on_text(message: Message):
    if arduino_mod.arduino and arduino_mod.arduino.is_open:
        try:
            arduino_mod.write(b'w')
            await message.answer("red LED OFF")
        except Exception as e:
            await message.answer(f"err: {e}")
    else:
        await message.answer("no conection")

@dp.message(F.text == "green 0")  
async def cmd_on_text(message: Message):
    if arduino_mod.arduino and arduino_mod.arduino.is_open:
        try:
            arduino_mod.write(b'e')
            await message.answer("green LED ON")
        except Exception as e:
            await message.answer(f"err: {e}")
    else:
        await message.answer("no conection")

@dp.message(F.text == "blue 0")  
async def cmd_on_text(message: Message):
    if arduino_mod.arduino and arduino_mod.arduino.is_open:
        try:
            arduino_mod.write(b'q')
            await message.answer("blue LED ON")
        except Exception as e:
            await message.answer(f"err: {e}")
    else:
        await message.answer("no conection")            #RGB OFF


@dp.message(F.text == "OFF ALL")  
async def cmd_on_text(message: Message):
    if arduino_mod.arduino and arduino_mod.arduino.is_open:
        try:
            arduino_mod.write(b'f')
            await message.answer("OFF ALL")
        except Exception as e:
            await message.answer(f"err: {e}")
    else:
        await message.answer("Нет связи")

@dp.message(F.text == "ON ALL")  
async def cmd_on_text(message: Message):
    if arduino_mod.arduino and arduino_mod.arduino.is_open:
        try:
            arduino_mod.write(b'o')
            await message.answer("ON ALL")
        except Exception as e:
            await message.answer(f"err: {e}")
    else:
        await message.answer("no conection")

                                                        #TODO: убрать тестовые приколы!!!!!!!


@dp.message(F.text == "beep")                           #beep!!!
async def cmd_off_text(message: Message):           
    if arduino_mod.arduino and arduino_mod.arduino.is_open:
        try:
            arduino_mod.write(b'd')
            await message.answer("BEEP!!!")                 #TODO: добавить кнопку на beep
        except Exception as e:
            await message.answer(f"err: {e}")
    else:
        await message.answer("no conection")

# @dp.message(F.text == "температура/влажность комнаты")
# async def cmd_off_text(message: Message):
#     if not arduino_mod.arduino or not arduino_mod.arduino.is_open:
#         await message.answer("no conection")
#         return

#     try:
#         arduino_mod.write(b't')
#         arduino_mod.flush()                                           #очистка буфера ос для предотврашения потери данных
#         response = await asyncio.to_thread(arduino_mod.readline)
        
#         if response:
#             temp = response.decode('utf-8', errors='ignore').strip()
#             await message.answer(temp)
#         else:
#             await message.answer("timeout")
            
#     except serial.SerialException as e:
#         await message.answer(f"err: {e}")
#     except Exception as e:
#         await message.answer(f"err: {e}")

@dp.message(F.text == "температура/влажность комнаты")
async def cmd_temp(message: Message):
    response = await asyncio.to_thread(arduino_mod.get_sensor_data)             #вызов из файла ардуино
    if response:
        await message.answer(response)
    else:
        await message.answer("Ошибка: нет связи или данных")


           
async def main():                   #connect
    connect()
    await dp.start_polling(bot)

if __name__ == '__main__':                  #start точка входа
    try:
        logging.basicConfig(level=logging.INFO)
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Бот остановлен")
        if arduino_mod.arduino:
            arduino_mod.arduino.close()
