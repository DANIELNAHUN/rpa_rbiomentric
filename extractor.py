import datetime
import os

import lackey
import pyautogui
from lackey import *


def extraer_data():
  of_nodescargados =[]
  of_descargadas =[]
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
        of_nodescargados.append(oficina)
        lackey.click(aceptar_no_conectado)
        time.sleep(1)
      else:
        time.sleep(60)
        lackey.click(desconectar)
        of_descargadas.append(oficina)
    else:
      print(f"No se encontro la oficina {oficina}")

  pyautogui.alert('Se termino de Analizar las Oficinas', title="RPA for Reporte Biometrico")

  with open('files/noDescargados.txt','a') as txt:
    txt.write(""+'\n')
    txt.write("Informe del dia: "+ datetime.datetime.now().strftime("%Y-%m-%d"))
    txt.write("Las oficinas que no se descargaron son:")
    for oficina in of_nodescargados:
      oficina_name, oficina_ext = oficina.split(".")
      txt.write("- "+oficina_name)
    txt.write("")
    txt.write(""+'\n')

  with open('files/Descargados.txt','a') as txt:
    txt.write(""+'\n')
    txt.write("Informe del dia: "+ datetime.datetime.now().strftime("%Y-%m-%d"))
    txt.write("Las oficinas que se descargaron son:")
    for oficina in of_descargadas:
      oficina_name, oficina_ext = oficina.split(".")
      txt.write("- "+oficina_name)
    txt.write("")
    txt.write(""+'\n')