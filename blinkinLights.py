from RPi import GPIO
from RPLCD import CharLCD
GPIO.cleanup()
lcd = CharLCD(numbering_mode=GPIO.BOARD, cols=16, rows=2, pin_rs=37, pin_e=35, pins_data=[33, 31, 29, 23])
lcd.clear()

def cToF(c: float) -> float:
  return c * (9.0/5) + 32

def fToC(f: float) -> float:
  return (f - 32) * (5.0/9)




