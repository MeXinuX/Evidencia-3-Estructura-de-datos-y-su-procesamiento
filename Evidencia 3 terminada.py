#################### IMPORTACION DE LIBRERIAS REQUERIDAS ####################

#Esta libreria la importamos para la creacion de animaciones
from __future__ import unicode_literals

#Esta libreria la importamos para la creacion de animaciones
from logging import exception

#Esta libreria la importamos para la creacion de animaciones
from halo import Halo

#Esta libreria la importamos para la manipulacion de base de datos
import sqlite3
from sqlite3 import Error

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

#Esta LIbreria la Importamos para el manejo de excel
import pandas as pd

####!!! ESTA LIBRERIA NO VIENE POR DEFECTO EN PYTHON HAY QUE INSTALARLA !!! ####

#Esta libreria la importamos para la creacion de animaciones
from tqdm import tqdm

#Esta libreria la importamos para la creacion de animaciones
from time import sleep


#COLORES PARA LA IMPRESION DE TEXTO EN PANTALLA
BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
RESET = '\033[35m'

#################### CREACION DE FUNCIONES PARA LAS ANIMACIONES ####################
def create_animation(mensaje):#Animacion De Creacion de un Cliente
    numero = 100
    print(GREEN + f"\n {mensaje}")
    for i in tqdm(range(numero)):
        sleep(0.01)
    sleep(0)
    os.system('clear')

def load_box(texto,mensaje):
    sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

    spinner = Halo(text=mensaje,color="blue", spinner="dots")

    try:
        spinner.start()
        time.sleep(4)
        spinner.succeed(texto)
    except (KeyboardInterrupt, SystemExit):
        spinner.stop()

def fail_load_box(texto,mensaje):
    sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

    spinner = Halo(text=mensaje,color="blue", spinner="dots")

    try:
        spinner.start()
        time.sleep(4)
        spinner.fail(texto)
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

try:
    with sqlite3.connect("SalasCoworking.db") as conn:
        mi_cursor = conn.cursor()
        mi_cursor.execute("CREATE TABLE IF NOT EXISTS clientes (id_cliente INTEGER NOT NULL PRIMARY KEY ,nombre_cliente TEXT NOT NULL);")
        mi_cursor.execute("CREATE TABLE IF NOT EXISTS salas (id_sala INTEGER  NOT NULL PRIMARY KEY,nombre_sala TEXT NOT NULL,cupo_sala INTEGER NOT NULL);")
        mi_cursor.execute("CREATE TABLE IF NOT EXISTS reservaciones (folio_reservacion INTEGER NOT NULL PRIMARY KEY ,fecha_reservacion TIMESTAMP NOT NULL,turno_reservacion text NOT NULL,fk_id_cliente INTEGER NOT NULL,fk_id_sala INTEGER NOT NULL,nombre_evento TEXT NOT NULL, FOREIGN KEY(fk_id_sala) REFERENCES salas(id_sala), FOREIGN KEY(fk_id_cliente) REFERENCES clientes(id_cliente));")
except Error as e:
    print (e)
except:
    print("☹ Ocurrio Un Error")

os.system('clear')
while True:
    #Limpieza De Pantalla
    print(BLACK + """\n
     -----------Menú de opciones----------
    |1)🎟️ Reservaciones                    |
    |2)🗃️ ​Reportes                         |
    |3)🛖 Registrar Una Sala               |
    |4)🚹​​Registrar Nuevo Cliente          |
    |5)✖ Salir                            |
     -------------------------------------""")
    menu = input("\nIngresa una opción del menú: ").strip()

    if menu not in "12345":
        print(RED + "⛔ Ingrese Una Opción Disponible Del Menú\n" + BLACK)
        continue

    #Salir
    if menu == "5":
        exit_animation()
        break

    #Reservaciones
    if menu == "1": #CURIEL/BARKIEL
        #Limpieza De Pantalla
        os.system('clear')

        while True:
            try:
                mi_cursor.execute("SELECT * FROM salas")
                registro_salas = mi_cursor.fetchall()

                mi_cursor.execute("SELECT * FROM clientes")
                registro_cliente = mi_cursor.fetchall()


                if not registro_salas:
                    print(RED + "⛔ No Se Encontró Ninguna Sala, Favor De Registrar Una.\n")
                    break

                if not registro_cliente:
                    print(RED + "⛔ No Se Encontró Ninguna Cliente, Favor De Registrar Uno.\n")
                    break

            except Error as e:
                print (e)
            except:
                print("☹ Ocurrio Un Error")

            print(BLACK + """\n
             --------------------Menú de opciones------------------
            |1)🆕Registrar Nueva Reservación                       |
            |2)✍ Modificar Descripcion De Una Reservación          |
            |3)🗓️ Consultar Disponibilidad De Salas Para Una Fecha  |
            |4)🗑️ Eliminar Una Reservación                          |
            |5)↩ Volver Al Menú Principal                          |
             ------------------------------------------------------""")
            sub_menu = input("\nIngresa una opción del menú: ").strip()

            if sub_menu not in "12345":
                print(RED + "⛔ Ingrese Una Opción Disponible Del Menú.\n" + BLACK)
                continue

            #Salir
            if sub_menu == "5":
                #Limpieza De Pantalla
                os.system('clear')
                break

            #Registrar Nueva Reservación
            if sub_menu == "1":
                #Limpieza De Pantalla
                os.system('clear')

                try:
                    mi_cursor.execute("SELECT * FROM clientes")
                    registro = mi_cursor.fetchall()

                    print(BLACK + "🆔 CLIENTE\t\tNOMBRE CLIENTE")
                    for id, nombre in registro:
                        print(f"{id}\t\t\t\t{nombre}")
                except Error as e:
                    print (e)
                except:
                    print(RED + "☹ Ocurrio Un Error")


                while True:
                    id_cliente = input(BLACK + "Ingrese Su 🆔 De Cliente:  ").strip()
                    if id_cliente == "":
                        print(RED + "⛔ Debe Ingresar Un 🆔.\n")
                        continue

                    if id_cliente.isspace():
                        print(RED + "⛔ Debe Ingresar Un 🆔.\n")
                        continue

                    if (not re.match("^[0-9]*$", id_cliente)):
                        print(RED + "⛔ El 🆔 del cliente Debe Ser Un Número, Intente De Nuevo.\n")
                        continue

                    id_cliente = int(id_cliente)

                    try:
                        valores = {"id_cliente":id_cliente}
                        mi_cursor.execute("SELECT id_cliente FROM clientes WHERE id_cliente = :id_cliente", valores)
                        registro = mi_cursor.fetchall()

                        if not registro:
                            print(RED + "⛔ No se encontró su 🆔 de cliente, Favor De Registrarse Como Cliente. \n")
                            break

                    except Error as e:
                        print (e)
                    except:
                        print(RED + "☹ Ocurrio Un Error")

                    try:
                        mi_cursor.execute("SELECT * FROM salas ORDER BY id_sala")
                        registro = mi_cursor.fetchall()

                        if not registro:
                            print(RED + "⛔ No Se Encontró Ninguna Sala, Favor De Registrar Una.\n")
                            break
                        else:
                            print(BLACK + "🆔 SALA\t\tNOMBRE SALA\tCUPO")
                            for id, nombre,cupo in registro:
                                print(f"{id}\t\t{nombre}\t\t{cupo}")
                    except Error as e:
                        print (e)
                    except:
                        print(RED + "☹ Ocurrio Un Error")


                    while True:
                        sala = input("Seleccione una sala:  ").strip()

                        if sala == "":
                            print(RED + "⛔ Debe seleccionar una sala. \n")
                            continue

                        if sala.isspace():
                            print(RED + "⛔ Debe seleccionar una sala. \n")
                            continue

                        if(not re.match("^[0-9]*$",sala)):
                            print(RED + "⛔ El 🆔 de la sala es un número, intente de nuevo. \n")
                            continue

                        sala = int(sala)
                        break
                    while True:
                        fecha_reservacion = input(BLACK + "🗓️ Ingrese la fecha deseada con el formato (dd/mm/aaaa): \n").strip()
                        if fecha_reservacion == "":
                            print(RED + "⛔ Debe ingresar una fecha.\n")
                            continue

                        if fecha_reservacion.isspace():
                            print(RED + "⛔ Debe ingresar una fecha. \n")
                            continue

                        if(not re.match("^[0-9]{2}/[0-9]{2}/[0-9]{4}$",fecha_reservacion)):
                            print(RED + "⛔ La fecha debe tener el formato(dd/mm/aaaa). \n")
                            continue

                        try:
                            fecha_reservacion = datetime.datetime.strptime(fecha_reservacion,"%d/%m/%Y").date()
                        except:
                            print(RED + "⛔ La fecha ingresada no es una fecha válida, intente de nuevo. \n")
                            continue

                        fecha_actual = (datetime.date.today())
                        limite_fecha = (fecha_reservacion - fecha_actual).days
                        if limite_fecha <=2:
                            print(RED + "⛔ Se necesitan más de 2 días de anticipación. \n")
                            continue
                            #mostrar_reservaciones(fecha_reservacion)
                        break

                    while True:
                        turno = input(BLACK + """\n
                        ----------Turnos----------
                        ( 🅼  )🌥️ Matutino
                        ( 🆅  )☀️ Vespertino
                        ( 🅽  )🌜 Nocturno
                        ( 🆂  )✖ Salir
                        --------------------------\nSeleccione un turno:  """).upper().strip()

                        if turno not in "MVNS":
                            print(RED + "⛔ Debes seleccionar una opción disponible en el menú, intenta de nuevo. \n")
                            continue

                        if turno == "":
                            print(RED + "⛔ Debe Seleccionar un turno. \n")
                            continue

                        if turno.isspace():
                            print(RED + "⛔ Debe Seleccionar un turno. \n")
                            continue

                        if turno == "S":
                            break

                        if turno == "M":
                            turno="Matutino"

                        if turno == "V":
                            turno="Vespertino"

                        if turno == "N":
                            turno="Nocturno"

                        try:
                            criterios = {"fecha":fecha_reservacion,"turno":turno}
                            mi_cursor.execute("SELECT fecha_reservacion,turno_reservacion FROM reservaciones WHERE DATE(fecha_reservacion) == :fecha AND turno_reservacion=:turno;", criterios)
                            #mi_cursor.execute("SELECT clave, nombre, fecha_registro FROM Amigo WHERE DATE(fecha_registro) >= :fecha;", criterios)
                            registros = mi_cursor.fetchall()

                            if registros:
                                print(RED + "⛔ Ya existe una reservación en ese turno, favor de ingresar otro turno. \n")
                                continue

                            while True:
                                nombre_evento = input(BLACK + "Ingrese el nombre del evento:  ").title()
                                if nombre_evento == "":
                                    print(RED + "⛔ Debe ingresar un nombre del evento. \n")
                                    continue
                                if nombre_evento.isspace():
                                    print(RED + "⛔ Debe ingresar un nombre del evento. \n")
                                    continue
                                break

                            reservaciones = (fecha_reservacion,turno,id_cliente,sala,nombre_evento)
                            mi_cursor.execute("INSERT INTO reservaciones (fecha_reservacion,turno_reservacion,fk_id_cliente,fk_id_sala,nombre_evento) VALUES(?,?,?,?,?)", reservaciones)
                            mi_cursor.execute("SELECT MAX(folio_reservacion),fecha_reservacion,turno_reservacion,fk_id_cliente,fk_id_sala,nombre_evento FROM reservaciones;")
                            reservacion_creada = mi_cursor.fetchall()

                            print("Reservacion Creada Con Exito")

                            print(BLACK + "FOLIO RESERVACION\t\tFECHA RESERVACION\t\tTURNO\t\tID CLIENTE\t\tID SALA\t\tNOMBRE DEL EVENTO")
                            for fol, fecha,turno,cliente,sala,evento in reservacion_creada:
                                print(f"{fol}\t\t\t\t{fecha}\t\t\t{turno}\t{cliente}\t\t\t{sala}\t\t{evento}")

                        except sqlite3.Error as e:
                            print (e)
                        except Exception:
                            print(RED + "☹ Ocurrio Un Error")
                        break
                    break

            #Modificar Descripcion
            if sub_menu == "2":
                #Limpieza De Pantalla
                os.system('clear')

                while True:
                    folio = input(BLACK + "Ingrese El Folio De Reservacion: ").strip()
                    if folio == "":
                        print(RED + "⛔ Debe Ingresar El Folio De Reservacion.\n")
                        continue

                    if folio.isspace():
                        print(RED + "⛔ Debe Ingresar El Folio De Reservacion.\n")
                        continue

                    if(not re.match("^[0-9]*$",folio)):
                        print(RED + "⛔ El Folio De Reservacion Debe Ser Un Numero.\n")
                        continue
                    folio = int(folio)
                    try:
                        valores = {"folio_reservacion":folio}
                        mi_cursor.execute("SELECT nombre_evento FROM reservaciones WHERE folio_reservacion = :folio_reservacion", valores)
                        registro = mi_cursor.fetchall()

                        if not registro:
                            print(RED + "⛔ No se encontró Una Reservación Con Ese Folio.\n")
                            break

                        nombre_antiguo=""
                        for nombre in registro:
                            nombre_antiguo=nombre
                    except Error as e:
                        print (e)
                    except:
                        print(RED + "☹ Ocurrio Un Error")
                        break

                    while True:
                        nuevo_nombre = input(BLACK + "Ingrese El Nuevo Nombre De Su Evento: ").title().strip()
                        if nuevo_nombre == "":
                            print(RED + "⛔ Debe Ingresar Un Nombre Del Evento.\n")
                            continue
                        if nuevo_nombre.isspace():
                            print(RED + "⛔ Debe Ingresar Un Nombre Del Evento.\n")
                            continue

                        mi_cursor.execute('UPDATE reservaciones SET nombre_evento = (?) WHERE folio_reservacion=(?);',[nuevo_nombre,folio])
                        conn.commit()

                        print("Se modifico el nombre del evento.")
                        print(f"Nombre Anterior: {nombre_antiguo}\nNombre Nuevo: {nuevo_nombre}")
                        break
                    break

            #Consultar Disponibilidad
            if sub_menu == "3":
                #Limpieza De Pantalla
                os.system('clear')
                while True:
                    fecha_consulta = input(BLACK + '¿Qué fecha desea consultar?: ')
                    if fecha_consulta == "":
                        print(RED + "⛔ Debe Ingresar una Fecha.\n")
                        continue

                    if(not re.match("^[0-9]{2}/[0-9]{2}/[0-9]{4}$",fecha_consulta)):
                        print(RED +"⛔ La fecha debe tener el formato(dd/mm/aaaa).\n")
                        continue

                    try:
                        fecha_consulta = datetime.datetime.strptime(fecha_consulta,"%d/%m/%Y").date()
                    except:
                        print(RED + "⛔ La Fecha Ingresada No es una Fecha Valida, Intente De Nuevo.\n")
                        continue

                    try:
                        criterios = {"fecha":fecha_consulta}
                        mi_cursor.execute("SELECT turno_reservacion, fk_id_sala FROM reservaciones WHERE DATE(fecha_reservacion) == :fecha;", criterios)
                        reservaciones_encontrados = mi_cursor.fetchall()

                        combinacion_reservas_encontradas = set(reservaciones_encontrados)

                        turnos = ["Matutino","Vespertino","Nocturno"]

                        mi_cursor.execute("SELECT id_sala FROM salas")
                        salas_encontradas = mi_cursor.fetchall()

                        salas_finales = []
                        for salas in salas_encontradas:
                            sala = salas[0]
                            salas_finales.append(sala)

                        reservaciones_posibles = []
                        for sala in salas_finales:
                            for turno in turnos:
                                reservaciones_posibles.append((turno,sala))
                            combinaciones_reservas_posibles = set((reservaciones_posibles))

                        reservas_posibles = set((combinaciones_reservas_posibles - combinacion_reservas_encontradas))

                        print('SALA      TURNO')
                        for turno,sala in reservas_posibles:
                            print(f'{sala}        {turno}')

                        break

                    except sqlite3.Error as e:
                        print(e)
                    except:
                        print("☹ Ocurrio Un Error")
                    break

            #Eliminar Una Reservación
            if sub_menu == "4":
                #Limpieza De Pantalla
                os.system('clear')

                while True:
                    try:
                        mi_cursor.execute("SELECT * FROM reservaciones")
                        registro = mi_cursor.fetchall()

                        if not registro:
                            print("⛔ No Existe Ninguna Reservacion, Favor De Registrar Una.\n")
                            break
                    except Error as e:
                        print (e)
                    except:
                        print("☹ Ocurrio Un Error")

                    folio = input("Ingrese El Folio De Reservacion: ").strip()
                    if folio == "":
                        print(RED + "⛔ Debe Ingresar El Folio De Reservacion.\n" + BLACK)
                        continue

                    if folio.isspace():
                        print(RED + "⛔ Debe Ingresar El Folio De Reservacion.\n" + BLACK)
                        continue

                    if(not re.match("^[0-9]*$",folio)):
                        print(RED + "⛔ El Folio De Reservacion Debe Ser Un Numero.\n" + BLACK)
                        continue
                    folio = int(folio)
                    try:
                        valores = {"folio_reservacion":folio}
                        mi_cursor.execute("SELECT * FROM reservaciones WHERE folio_reservacion = :folio_reservacion", valores)
                        registross = mi_cursor.fetchall()

                        if not registross:
                            print(RED + "⛔ No se encontró Una Reservación Con Ese Folio.\n")
                            break
                        else:
                            for folio, fecha,turno,cliente,sala,evento in registross:
                                print(BLACK +"Folio Reservacion: "+ GREEN , folio)
                                print(BLACK + "Fecha Reservacion: "+ GREEN , fecha)
                                print(BLACK + "Turno: "+ GREEN , turno)
                                print(BLACK + "🆔 Cliente: "+ GREEN , cliente)
                                print(BLACK + "🆔 Sala: "+ GREEN , sala)
                                print(BLACK + "Nombre Del Evento: "+ GREEN , evento)

                            while True:
                                decision = input(RED + "⚠️ ‼" + BLACK + " Esta Seguro Que desea Eliminar Esta Reservación "+ RED+"‼" + BLACK + " S/N:").upper().strip()

                                if decision not in "SN":
                                    print(RED + "⛔ Debes Seleccionar Una Opción Disponible Del Menú.\n")
                                    continue

                                if decision =="N":
                                    break

                                if decision =="":
                                    print(RED + "⛔ Debe Seleccionar una Opción.\n")

                                if decision.isspace():
                                    print(RED + "⛔ Debe Seleccionar una Opción.\n")
                                    continue

                                if decision == "S":
                                    mi_cursor.execute("DELETE FROM reservaciones WHERE folio_reservacion = :folio_reservacion", valores)
                                    print("Se Ha eliminado La Reservacion.")
                                    break
                    except Error as e:
                        print (e)
                    except:
                        print("☹ Ocurrio Un Error")
                    break

    #Reportes
    if menu == "2": #CURIEL/BARKIEL
        #Limpieza De Pantalla
        os.system('clear')
        while True:
            try:
                mi_cursor.execute("SELECT * FROM reservaciones ORDER BY folio_reservacion")
                registro = mi_cursor.fetchall()

                if not registro:
                    print(RED + "⛔ No Se Encontró Ninguna Reservacion, Favor De Registrar Una.\n")
                    break
            except Error as e:
                print (e)
            except:
                print("☹ Ocurrio Un Error")

            print(BLACK + """\n
             ---------------------Menú de opciones------------------
            |  1)🗒️ Reporte Reservaciones                            |
            |  2)📤Exportar Reporte Tabular A Excel                 |
            |  3)↩ Volver Al Menú Principal                         |
             -------------------------------------------------------""")
            sub_menu = input(BLACK + "\nIngresa una opción del menú: ")

            if sub_menu not in "123":
                print(RED + "⛔ Ingrese Una Opción Disponible Del Menú.\n")
                os.system('clear')
                continue

            #Salir
            if sub_menu == "3":
                break

            #Reporte Reservaciones
            if sub_menu == "1":
                while True:
                    fecha_consulta = input(BLACK + "Fecha de las reservaciones a consultar : ")
                    if fecha_consulta == "":
                        print(RED + "⛔ Debe Ingresar una Fecha.\n")
                        continue

                    if(not re.match("^[0-9]{2}/[0-9]{2}/[0-9]{4}$",fecha_consulta)):
                        print(RED + "⛔ La fecha debe tener el formato(dd/mm/aaaa).\n" )
                        continue
                    try:
                        fecha_consulta = datetime.datetime.strptime(fecha_consulta,"%d/%m/%Y").date()
                    except:
                        print(RED + "⛔ La Fecha Ingresada No es una Fecha Valida, Intente De Nuevo.\n")
                        continue

                    try:
                            criterios = {"fecha":fecha_consulta}
                            mi_cursor.execute("SELECT * FROM reservaciones WHERE DATE(fecha_reservacion) = :fecha;", criterios)
                            registros = mi_cursor.fetchall()

                            if not registros:
                                fail_load_box("Ningun Encontrado","Buscando Eventos")
                                print(RED + "⛔ No Se Encontró Ninguna Reservacion, En Esa Fecha.\n")
                                break


                            load_box("Eventos Encontrados","Buscando Eventos")
                            print(BLACK + "FOLIO RESERVACION\t\tFECHA RESERVACION\t\tTURNO\t\t🆔 CLIENTE\t\t🆔 SALA\t\tNOMBRE DEL EVENTO")
                            for fol, fecha,turno,cliente,sala,evento in registro:
                                print(f"{fol}\t\t\t\t{fecha}\t\t\t{turno}\t{cliente}\t\t\t{sala}\t\t{evento}")
                            break

                    except sqlite3.Error as e:
                        print (e)
                        break
                    except Exception:
                        print("☹ Ocurrio Un Error")
                        break

            #Excel
            if sub_menu == "2":
                while True:
                    fecha_consulta = input(BLACK + "Fecha de las reservaciones a consultar : ")
                    if fecha_consulta == "":
                        print(RED + "⛔ Debe Ingresar una Fecha.\n")
                        continue
                    if(not re.match("^[0-9]{2}/[0-9]{2}/[0-9]{4}$",fecha_consulta)):
                        print(RED + "⛔ La fecha debe tener el formato(dd/mm/aaaa).\n")
                        continue
                    try:
                        fecha_consulta = datetime.datetime.strptime(fecha_consulta,"%d/%m/%Y").date()
                    except:
                        print(RED + "⛔ La Fecha Ingresada No es una Fecha Valida, Intente De Nuevo.\n")
                        continue

                    try:
                        criterios = {"fecha":fecha_consulta}
                        mi_cursor.execute("SELECT * FROM reservaciones WHERE DATE(fecha_reservacion) = :fecha;", criterios)

                        registros = mi_cursor.fetchall()

                        if  not registros:
                            print(RED + "⛔ No Se Encontró Ninguna Reservacion, En Esa Fecha.\n")
                            break

                        registros_DataFrame = pd.DataFrame(registros)
                        registros_DataFrame.columns = ["FOLIO RESERVACION", "FECHA RESERVACION", "TURNO","ID CLIENTE","ID SALA","NOMBRE DEL EVENTO"]
                        registros_excel = registros_DataFrame.to_excel("Reporte Salas Coworking.xlsx")
                        break
                    except sqlite3.Error as e:
                        print (e)
                    except Exception:
                        print("☹ Ocurrio Un Error")
                        break

    #Registrar Una Sala
    if menu == "3": #XIMENA
        os.system('clear')
        while True:
            nombre_sala = input(BLACK + "Ingrese el nombre de la sala:  ").title().strip()
            if nombre_sala == "":
                print(RED + "⛔ Debe Ingresar Un Nombre A La Sala.\n")
                continue

            if nombre_sala.isspace():
                print(RED + "⛔ Debe Ingresar Un Nombre A La Sala.\n")
                continue

            """ nombre_existente = "" #Preguntar como puede ser una forma mas pythonica
            for clave,valor in salas.items():
                if nombre_sala == valor[0]:
                    nombre_existente = valor[0]

            if nombre_sala == nombre_existente:
                print(RED + "Ya existe una sala con ese nombre, Registre otro Nombre" + BLACK)
                continue """

            while True:
                cupo_sala = ""
                try:
                    cupo_sala = int(input(BLACK + "Ingrese el cupo de la sala:  "))
                except:
                    if cupo_sala == "":
                        print(RED + "⛔ Debe Ingresar El Cupo De La Sala.\n")
                        continue
                    if cupo_sala.isspace():
                        print(RED + "⛔ Debe Ingresar El Cupo De La Sala.\n")
                        continue
                    print(RED + "⛔ Solamente se aceptan números.\n")
                    continue
                else:
                    mi_cursor.execute("INSERT INTO salas (nombre_sala,cupo_sala) VALUES (?,?);", [nombre_sala,cupo_sala])
                    conn.commit()
                    try:
                        mi_cursor.execute("SELECT MAX(id_sala),nombre_sala,cupo_sala FROM salas WHERE nombre_sala=(?);", [nombre_sala])
                        registros = mi_cursor.fetchall()


                        create_animation("Registrando Sala")

                        for idsala, nombre,cupo in registros:
                            print(BLACK + "🆔 Sala: "+ GREEN + f"{idsala}")
                            print(BLACK + "Nombre De La Sala: "+ GREEN + f"{nombre}")
                            print(BLACK + "Cupo: "+ GREEN + f"{cupo}")
                    except exception:
                        print("☹ Ocurrio Un Error")
                    break
            break

    #Registrar Un Cliente
    if menu == "4": #OSCAR
        os.system('clear')
        while True:
            nombre_cliente = input(BLACK + "Ingrese su nombre: ").title().strip()

            if nombre_cliente == "":#REVISAR ESPACIADO PARA EVITAR QUE EL USUARIO INGRESE NUMEROS Y PUEDA INGRESAR SOLO LETRAS
                print(RED + "⛔ El nombre No Puede Quedar Vacio.\n")
                continue

            if nombre_cliente.isspace():
                print(RED + "⛔ El nombre No Puede Quedar Vacio.\n")
                continue

            if (not re.match("^[a-zA-Z_ ñÑ]*$", nombre_cliente)):#Expresion Regular para validar que el usuario solamente ingrese palabras y no numeros con espacios
                print(RED + "⛔ El Nombre solo pueden ser Letras, Intente de Nuevo.\n")
                continue
            else:
                mi_cursor.execute("INSERT INTO clientes (nombre_cliente) VALUES (?);", [nombre_cliente])
                conn.commit()
            try:
                mi_cursor.execute("SELECT MAX(id_cliente),nombre_cliente FROM clientes WHERE nombre_cliente=(?);", [nombre_cliente])
                registros = mi_cursor.fetchall()
                create_animation("Registrando Cliente")
                for idcliente, nombre in registros:
                    print(BLACK + "Su 🆔 De Cliente:" + GREEN +  f"{idcliente}")
                    print(BLACK + "Su Nombre De Cliente: " + GREEN + f"{nombre}")
            except exception:
                print("☹ Ocurrio Un Error")

            break