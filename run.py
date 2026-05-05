import asyncio
import logging
import serial

from app.arduino import arduino
from app.arduino import connect
from aiogram import Bot,Dispatcher,F
from aiogram.filters import CommandStart,Command
from aiogram.types import Message
import app.keyboard as kb
from config import TOKEN

bot=Bot(token=TOKEN)
dp=Dispatcher()

ARDUINO_PORT = '/dev/ttyUSB0'
BAUD_RATE = 9600
arduino = None

def connect():# подключение к ардуино
    global arduino
    try:
        arduino = serial.Serial(ARDUINO_PORT, BAUD_RATE, timeout=1)
        print(f"success conect {ARDUINO_PORT}")
        return True
    except serial.SerialException as e:
        print(f"NOT conection: {e}")
        return False

def write(data: bytes):#отправка данных на ардуинку
    if arduino and arduino.is_open:
        arduino.write(data)

@dp.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer('привет!!!\nэтот бот используется для управления умным домом\n',
                         reply_markup=kb.main)#hi massage

@dp.message(F.text == "RGB MOD")#TODO:добавить выход из мода ргб ГОТОВО!!
async def helpGet(message: Message):
    await message.answer('RGB MOD ON!!!',
                         reply_markup=kb.rgb)
    
@dp.message(F.text == "Exit")#TODO:добавить выход из мода ргб ГОТОВО!!
async def helpGet(message: Message):
    await message.answer('RGB MOD OFF!!!',
                         reply_markup=kb.main)

@dp.message(F.text == "Включить свет")  
async def cmd_on_text(message: Message):#TODO: убрать отладочную шнягу со всех команд бота!!!!
    if arduino and arduino.is_open:
        try:
            arduino.write(b'1')
            await message.answer("LED ON")
        except Exception as e:
            await message.answer(f"err: {e}")
    else:
        await message.answer("no conection")

@dp.message(F.text == "Выключить свет")#TODO: добавить такую функцию для rgb led #ГОТОВО
async def cmd_off_text(message: Message):
    if arduino and arduino.is_open:
        try:
            arduino.write(b'0')
            await message.answer("LED OFF")
        except Exception as e:
            await message.answer(f"err: {e}")
    else:
        await message.answer("no conection")



@dp.message(F.text == "red")                    #RGB ON
async def cmd_on_text(message: Message):
    if arduino and arduino.is_open:
        try:
            arduino.write(b'r')
            await message.answer("red LED ON")
        except Exception as e:
            await message.answer(f"err: {e}")
    else:
        await message.answer("no conection")

@dp.message(F.text == "green")  
async def cmd_on_text(message: Message):
    if arduino and arduino.is_open:
        try:
            arduino.write(b'g')
            await message.answer("green LED ON")
        except Exception as e:
            await message.answer(f"err: {e}")
    else:
        await message.answer("no conection")

@dp.message(F.text == "blue")  
async def cmd_on_text(message: Message):
    if arduino and arduino.is_open:
        try:
            arduino.write(b'b')
            await message.answer("blue LED ON")
        except Exception as e:
            await message.answer(f"err: {e}")
    else:
        await message.answer("no conection")         #RGB ON




@dp.message(F.text == "red 0")                      #RGB OFF
async def cmd_on_text(message: Message):
    if arduino and arduino.is_open:
        try:
            arduino.write(b'w')
            await message.answer("red LED OFF")
        except Exception as e:
            await message.answer(f"err: {e}")
    else:
        await message.answer("no conection")

@dp.message(F.text == "green 0")  
async def cmd_on_text(message: Message):
    if arduino and arduino.is_open:
        try:
            arduino.write(b'e')
            await message.answer("green LED ON")
        except Exception as e:
            await message.answer(f"err: {e}")
    else:
        await message.answer("no conection")

@dp.message(F.text == "blue 0")  
async def cmd_on_text(message: Message):
    if arduino and arduino.is_open:
        try:
            arduino.write(b'q')
            await message.answer("blue LED ON")
        except Exception as e:
            await message.answer(f"err: {e}")
    else:
        await message.answer("no conection")            #RGB OFF


@dp.message(F.text == "OFF ALL")  
async def cmd_on_text(message: Message):
    if arduino and arduino.is_open:
        try:
            arduino.write(b'f')
            await message.answer("OFF ALL")
        except Exception as e:
            await message.answer(f"err: {e}")
    else:
        await message.answer("Нет связи")

@dp.message(F.text == "ON ALL")  
async def cmd_on_text(message: Message):
    if arduino and arduino.is_open:
        try:
            arduino.write(b'o')
            await message.answer("ON ALL")
        except Exception as e:
            await message.answer(f"err: {e}")
    else:
        await message.answer("no conection")


#TODO: убрать тестовые приколы!!!!!!!

@dp.message(F.text == "beep")                     #beep!!!
async def cmd_off_text(message: Message):           #TODO: добавить кнопку на beep
    if arduino and arduino.is_open:
        try:
            arduino.write(b'b')
            await message.answer("BEEP!!!")
        except Exception as e:
            await message.answer(f"err: {e}")
    else:
        await message.answer("no conection")

@dp.message(F.text == "температура/влажность комнаты")
async def cmd_off_text(message: Message):
    if not arduino or not arduino.is_open:
        await message.answer("no conection")
        return

    try:
        arduino.write(b't')
        arduino.flush()                                 #очистка буфера ос для предотврашения потери данных
        response = await asyncio.to_thread(arduino.readline)
        
        if response:
            temp = response.decode('utf-8', errors='ignore').strip()
            await message.answer(temp)
        else:
            await message.answer("timeout")
            
    except serial.SerialException as e:
        await message.answer(f"err: {e}")
    except Exception as e:
        await message.answer(f"err: {e}")
           
async def main():                   #connect
    connect()
    await dp.start_polling(bot)

if __name__ == '__main__':                  #start точка входа
    try:
        logging.basicConfig(level=logging.INFO)
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Бот остановлен")
        if arduino:
            arduino.close()
