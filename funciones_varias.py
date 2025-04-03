import os, json

def limpiar():
    os.system("cls" if os.name=="nt" else "clear")

def leer_json():
    with open("services.json","r") as file:
        servicios=json.load(file)
    return servicios

servicios=leer_json()

def mostrar_servicios():
    for servicio in servicios:
        print("---------------------------")
        for clave, valor in servicio.items():
            print(f"{clave}->{valor}")
        print("---------------------------")
