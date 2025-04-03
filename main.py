from menues import saludo
from menu import *

from funciones_varias import mostrar_servicios



saludo()
while True:
    op=menu_principal()
    match op:
        case "1":
            while True:
                from add_service import añadir_servicio
                op=reg_servicio()
                if op=="1": mostrar_servicios()
                elif op=="2": añadir_servicio()
                elif op=="3": break
                else: print("Ingrese una opcion valida")
        case "2":
            while True:
                op=mod_servicio()
                from edit_services import editar_servicios
                if op=="1": mostrar_servicios()
                elif op=="2": editar_servicios()
                elif op=="3": break
                else: print("Ingrese una opcion valida")

        case "3":
            while True:
                from delete_services import eliminar_servicios
                op=elim_servicio()
                if op=="1": mostrar_servicios()
                elif op=="2": eliminar_servicios()
                elif op=="3": break
                else: print("Ingrese una opcion valida")
        case "4":
            print("Saliendo")
            break
        case _:
            print("Ingrese una opcion valida")
