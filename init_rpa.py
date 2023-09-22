import os
import subprocess
import time

import lackey
import pyautogui
from lackey import *
from pynput.keyboard import Controller, Key

import extractor as ex

keyboard = Controller()

time.sleep(1)
program = "src/program.jpg"
name_proceess = "Att.exe"

#CERRANDO APLICACION PARA EVITAR ERRORES
subprocess.run(["taskkill","/F","/IM",name_proceess,"/T"])

#BUSCANDO IPS PARA CONECTARSE A LA VPN
ips_sedes =[
  {"ip":"181.65.232.26","sede":"ILO HFC"},
  {"ip":"181.65.232.27","sede":"ILO HFC"},
  {"ip":"181.65.232.28","sede":"ILO HFC"},
  {"ip":"181.65.232.29","sede":"ILO HFC"},
  {"ip":"181.65.232.30","sede":"ILO HFC"},
]
for ip_data in ips_sedes:
  command = ['ping', '-n', '1', ip_data['ip']]
  response_ip = subprocess.call(command)
  if response_ip == 0:
    print(f'La direccion IP:{ip_data["ip"]} responde')
  else:
    print(f'La direccion IP {ip_data["ip"]} no responde')

# ABRE EL PROGRAMA BUSCANDO EN EL ESCRITORIO
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
    pyautogui.alert('Por favor instale el Programa o agreguelo como acceso directo en el Escritorio :).', title="RPA for Reporte Biometrico")

