import time

import lackey
import pyautogui
from lackey import *
from pynput.keyboard import Controller, Key

keyboard = Controller()

time.sleep(1)

#ABRE EL PROGRAMA SI O SI
if lackey.exists('.\src\program.jpg'):
  lackey.doubleClick('.\src\program.jpg')
else:
  keyboard.press(Key.cmd)
  keyboard.press('d')
  keyboard.release(Key.cmd)
  keyboard.release('d')
  lackey.doubleClick('.\src\program.jpg')



