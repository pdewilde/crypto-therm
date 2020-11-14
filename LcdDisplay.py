from RPi import GPIO
from RPLCD import CharLCD
from CryptoThermLib import cToF, fToC
GPIO.cleanup()
lcd = CharLCD(numbering_mode=GPIO.BOARD, cols=16, rows=2, pin_rs=37, pin_e=35, pins_data=[33, 31, 29, 23])
lcd.clear()

# 0000000000000000
# CUR: 70F | State
# SET: 72F |   ON    # or OFF
def getTempAndStatusStr(curTemp: float, setTemp: float, unit: str, status: str) -> str:
    return "CUR:{:3.0f}{:1} | StateSET:{:3.0f}{:1} |{:>6}".format(curTemp, unit, setTemp, unit, status)

GPIO.cleanup()

