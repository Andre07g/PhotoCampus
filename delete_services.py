import json

def leer_servicios():
    with open ("services.json","r") as file:
        servicios=json.load(file)
    return servicios

servicios = leer_servicios()

def escribir_servicios():
    with open ("services.json", "w") as file:
        json.dump(servicios, file, indent=4)

def eliminar_servicios():
    servicioexiste=False
    nom_servicio=input("Ingrese el nombre del servicio: ")
    for servicio in servicios:
        for clave, valor in servicio.items():
            if clave == "Nombre_paquete" and valor == nom_servicio:
                servicioexiste=True
                indice=servicios.index(servicio)
    if servicioexiste==False: print("El servicio que ingresó no existe! ")
    else:
        servicios.pop(indice)
        escribir_servicios()
        print("El servicio se ha eliminado correctamente!")

eliminar_servicios()