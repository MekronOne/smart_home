import serial

ARDUINO_PORT = '/dev/ttyUSB0'
BAUD_RATE = 9600
arduino = None

def connect():
    global arduino
    try:
        arduino = serial.Serial(ARDUINO_PORT, BAUD_RATE, timeout=1)#com otlad
        #print(f"success conect {ARDUINO_PORT}")
        return True
    except serial.SerialException as e:
        #print(f"NOT conection: {e}")
        return False

def write(data: bytes):
    if arduino and arduino.is_open:
        arduino.write(data)