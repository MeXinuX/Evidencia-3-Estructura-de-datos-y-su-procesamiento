#################### IMPORTACION DE LIBRERIAS REQUERIDAS ####################
from ast import While
import sqlite3
import sys
from sqlite3 import Error

from __future__ import unicode_literals

from curses.ascii import isspace
from turtle import color
from halo import Halo

#Esta libreria la importamos para realizar validaciones
import re

#Esta libreria la importamos para realizar validacion de fecha posible al momento de hacer una reservacion
import datetime

#Esta libreria la importamos para la creacion de animaciones
import time

#Esta libreria la importamos para la creacion de animaciones
import sys

#Esta libreria la importamos para el uso de CSV
import os

#Esta libreria la importamos para el uso de CSV
import csv

#Esta LIbreria la Importamos para el manejo de excel
import pandas as pd

####!!! ESTA LIBRERIA NO VIENE POR DEFECTO EN PYTHON HAY QUE INSTALARLA !!! ####
from tqdm import tqdm #Esta libreria la importamos para la creacion de animaciones
from time import sleep #Esta libreria la importamos para la creacion de animaciones


#COLORES PARA LA IMPRESION DE TEXTO EN PANTALLA
BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
RESET = '\033[35m'

#################### CREACION DE FUNCIONES PARA LAS ANIMACIONES ####################
def create_client_animation():#Animacion De Creacion de un Cliente
    numero = 100
    print(GREEN + "\n Registrando Nuevo Cliente")
    for i in tqdm(range(numero)):
        sleep(0.01)
    sleep(0)
    os.system('clear')

def load_box(texto):
    sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

    success_message="Cargando Datos"
    failed_message="Loading failed"
    unicorn_message="Loading unicorn"

    spinner = Halo(text=success_message,color="blue", spinner="dots")

    try:
        spinner.start()
        time.sleep(4)
        spinner.succeed(texto)
    except (KeyboardInterrupt, SystemExit):
        spinner.stop()

def exit_animation():#Animacion de cerrado de programa
    sys.stdout.write('\rSaliendo')
    time.sleep(0.2)
    sys.stdout.write('\rSaliendo.')
    time.sleep(0.2)
    sys.stdout.write('\rSaliendo..')
    time.sleep(0.2)
    sys.stdout.write('\rSaliendo...')
    time.sleep(0.2)
    sys.stdout.write('\rSaliendo....')
    time.sleep(0.2)
    os.system('clear')

def search_animation():
    sys.stdout.write('\rBuscando Eventos En esa Fecha')
    time.sleep(0.3)
    sys.stdout.write('\rBuscando Eventos En esa Fecha.')
    time.sleep(0.3)
    sys.stdout.write('\rBuscando Eventos En esa Fecha..')
    time.sleep(0.3)
    sys.stdout.write('\rBuscando Eventos En esa Fecha...')
    time.sleep(0.3)
    sys.stdout.write('\rBuscando Eventos En esa Fecha....')
    time.sleep(0.3)
    sys.stdout.write('\rBuscando Eventos En esa Fecha    ')
    time.sleep(0.3)
    sys.stdout.write('\rBuscando Eventos En esa Fecha.   ')
    time.sleep(0.3)
    sys.stdout.write('\rBuscando Eventos En esa Fecha..  ')
    time.sleep(0.3)
    sys.stdout.write('\rBuscando Eventos En esa Fecha... ')
    time.sleep(0.3)
    sys.stdout.write('\rBuscando Eventos En esa Fecha....')
    time.sleep(0.3)
    sys.stdout.write('\r                                 \n')

def load_animation():#Animacion de carga de archivos
    sys.stdout.write('\rCargando')
    time.sleep(0.3)
    sys.stdout.write('\rCargando.')
    time.sleep(0.3)
    sys.stdout.write('\rCargando..')
    time.sleep(0.3)
    sys.stdout.write('\rCargando...')
    time.sleep(0.3)
    sys.stdout.write('\rCargando....')
    time.sleep(0.3)
    sys.stdout.write('\rCargando    ')
    time.sleep(0.3)
    sys.stdout.write('\rCargando.   ')
    time.sleep(0.3)
    sys.stdout.write('\rCargando..'  )
    time.sleep(0.3)
    sys.stdout.write('\rCargando... ')
    time.sleep(0.3)
    sys.stdout.write('\rCargando....')
    time.sleep(0.2)
    sys.stdout.write(GREEN + '\r¡Carga De Información Completada!\n' + BLACK)


while True:
    print(BLACK + """\n
     -----------Menú de opciones----------
    |  1) Reservaciones                    |
    |  2) Reportes                         |
    |  3) Registrar Una Sala               |
    |  4) Registrar Nuevo Cliente          |
    |  5) Salir                            |
     -------------------------------------""")
    menu = input("\nIngresa una opción del menú: ")
    if menu not in "12345":
        print("Ingrese Una Opción Disponible Del Menú")
        continue

    #Salir
    if menu == "5":
        exit_animation()
        break

    #Reservaciones
    if menu == "1": #CURIEL/BARKIEL
        print(BLACK + """\n
         --------------------Menú de opciones-------------------
        |  1) Registrar Nueva Reservación                       |
        |  2) Modificar Descripcion De Una Reservación          |
        |  3) Consultar Disponibilidad De Salas Para Una Fecha  |
        |  4) Eliminar Una Reservación                          |
        |  5) Volver Al Menú Principal                          |
         -------------------------------------------------------""")
        sub_menu = input("\nIngresa una opción del menú: ")

        if sub_menu not in "12345":
            print("Ingrese Una Opción Disponible Del Menú")
            continue

        #Salir
        if sub_menu == "5":
            break

        #Registrar Nueva Reservación
        if sub_menu == "1":
            break

        #Modificar Descripcion
        if sub_menu == "2":
            break

        #Consultar Disponibilidad
        if sub_menu == "3":
            break

        #Eliminar Una Reservación
        if sub_menu == "4":
            break

    #Reportes
    if menu == "2": #CURIEL/BARKIEL
        print(BLACK + """\n
         --------------------Menú de opciones-------------------
        |  1) Reporte Reservaciones                             |
        |  2) Exportar Reporte Tabular A Excel                  |
        |  3) Volver Al Menú Principal                          |
         -------------------------------------------------------""")
        sub_menu = input("\nIngresa una opción del menú: ")

        if sub_menu not in "123":
            print("Ingrese Una Opción Disponible Del Menú")
            continue

        #Salir
        if sub_menu == "3":
            break

        #Reporte Reservaciones
        if sub_menu == "1":
            break

        #Excel
        if sub_menu == "2":
            break


    #Registrar Una Sala
    if menu == "3": #XIMENA
        print()

    #Registrar Un Cliente
    if menu == "4": #OSCAR
        print()