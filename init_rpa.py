import os
import time

import lackey
import subprocess
import pyautogui
from lackey import *
from pynput.keyboard import Controller, Key

import extractor as ex

keyboard = Controller()

time.sleep(1)
program = "src/program.jpg"
name_proceess = "Att.exe"
subprocess.run(["taskkill","/F","/IM",name_proceess,"/T"])
#ABRE EL PROGRAMA BUSCANDO EN EL ESCRITORIO
if lackey.exists(program):
  lackey.doubleClick(program)
  time.sleep(2)
  ex.extraer_data()
else:
  keyboard.press(Key.cmd)
  keyboard.press('d')
  keyboard.release(Key.cmd)
  keyboard.release('d')
  if lackey.exists(program):
    lackey.doubleClick(program)
    time.sleep(2)
    ex.extraer_data()
  #SI NO ENCUENTRA EL PROGRAMA EN EL ESCRITORIO
  else:
    pyautogui.alert('Por favor instale el Programa o agreguelo como acceso directo en el Escritorio :).', title="RPA for Reporte Biometrico", timeout=10)

