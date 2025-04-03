import json

def leer_servicio():
    with open ("services.json","r") as file:
        servicios=json.load(file)
    return servicios

servicios=leer_servicio()

def escribir_servicio():
    with open ("services.json","w") as file:
        json.dump(servicios, file, indent=4)

def añadir_servicio():
    servicioexiste=False
    nom_servicio=input("Ingrese nombre del servicio a añadir: ").strip().lower()
    for servicio in servicios:
        for clave, valor in servicio.items():
            if clave=="Nombre_paquete" and valor==nom_servicio:
                servicioexiste=True
    if servicioexiste==True: print("El servicio ya existe")
    else:
        precio=int(input("Ingrese el precio del servicio: "))
        tipoevento=input("Ingrese el tipo de evento: ")
        horas=float(input("Ingrese la cantidad de horas del servicio: "))
        servicios.append({"Nombre_paquete":nom_servicio,
                          "Precio":precio,
                          "Evento":tipoevento,
                          "Duracion":horas})
        escribir_servicio()
        print("El servicio ha sido añadido correctamente")

añadir_servicio()