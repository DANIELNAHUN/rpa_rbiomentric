import os

import lackey
import pyautogui
from lackey import *


def extraer_data():
  #CONECTAR LAS SEDES
  path = 'src/oficinas'
  oficinas = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
  cant_oficinas = len(oficinas)
  print(f"Se tiene {cant_oficinas} oficinas registradas.")

  for oficina in oficinas:
    obj_oficina = str("src/oficinas/"+oficina)
    if lackey.exists(obj_oficina):
      print(f"La oficina de {oficina} existe")
    else:
      print(f"No se encontro la oficina {oficina}")

  pyautogui.alert('Se termino de Analizar las Oficinas', title="RPA for Reporte Biometrico", timeout=3)