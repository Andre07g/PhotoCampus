import json

def leer_servicios():
    with open("services.json","r") as file:
        servicios=json.load(file)
    return servicios

servicios=leer_servicios()

def escribir_servicios():
    with open("services.json","w") as file:
        json.dump(servicios, file, indent=4)

def editar_servicios():
    servicioexiste=False
    nom_servicio=input("Ingrese nombre del paquete: ")
    for servicio in servicios:
        for clave, valor in servicio.items():
            if clave=="Nombre_paquete" and valor==nom_servicio:
                servicioexiste=True
                indice=servicios.index(servicio)
    if servicioexiste==False: print("El servicio ingresado no existe")
    else:
        while True:
            try:
                precio=int(input("Ingrese el nuevo precio del servicio: "))
                break
            except:
                print("Digite una cantidad valida")
        tipoevento=input("Ingrese el tipo de evento: ")
        while True:
            try:
                horas=float(input("Ingrese las horas del evento: "))
                break
            except: print("Digite una cantidad valida")
        servicios[indice]={"Nombre_paquete":nom_servicio,
                          "Precio":precio,
                          "Evento":tipoevento,
                          "Duracion":horas}
        escribir_servicios()
        print("El servicio fue editado correctamente")
    