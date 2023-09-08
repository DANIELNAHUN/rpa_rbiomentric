import os

import lackey
import pyautogui
from lackey import *


def extraer_data():
  of_sinacceso =[]
  #CONECTAR LAS SEDES
  path = 'src/oficinas'
  conectar = 'src/conectar.jpg'
  desconectar = 'src/desconectar.jpg'
  descargar = 'src/descargar.jpg'
  aviso_no_conectado= 'src/no-conectado.jpg'
  aceptar_no_conectado = 'src/aceptar-no-oficina.jpg'
  oficinas = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
  cant_oficinas = len(oficinas)
  print(f"Se tiene {cant_oficinas} oficinas registradas.")

  for oficina in oficinas:
    obj_oficina = str("src/oficinas/"+oficina)
    if lackey.exists(obj_oficina):
      lackey.click(obj_oficina)
      time.sleep(1)
      lackey.click(conectar)
      time.sleep(15)
      lackey.click(descargar)
      time.sleep(1)
      if lackey.exists(aviso_no_conectado):
        of_sinacceso.append(obj_oficina)
        lackey.click(aceptar_no_conectado)
        time.sleep(1)
      else:
        time.sleep(60)
        lackey.click(desconectar)        
    else:
      print(f"No se encontro la oficina {oficina}")

  pyautogui.alert('Se termino de Analizar las Oficinas', title="RPA for Reporte Biometrico")
  print(of_sinacceso)