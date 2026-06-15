import serial
ARDUINO_PORT = 'COM3'
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

def get_sensor_data():
    global arduino
    if arduino and arduino.is_open:
        #arduino.reset_input_buffer() 
        arduino.write(b't')
        arduino.flush() 
        line = arduino.readline().decode('utf-8', errors='ignore').strip()
        return line
    return None

def send_command(char: str):
    global arduino
    if arduino and arduino.is_open:
        arduino.write(char.encode())
        return True
    return False
