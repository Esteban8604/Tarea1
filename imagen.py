import requests
import threading
import os


def request(URL, nombre):
    """
    descarga las imagenes
    arguments:
        (URL)str La imagen que va a descargar
        (nombre)str nombre que les va a colocar a las imagenes
    returns:
    """
    respuesta = requests.get(URL)

    carpeta_imagenes = os.getcwd() + "\img" #--------------Asigna la direccion de la carpeta a una variable

    if os.path.exists(carpeta_imagenes):#------------------Verifica si la carpeta existe
        direccion = os.path.join(carpeta_imagenes, nombre)#Coloca la direccion y el nombre
    else:
        os.mkdir("img")#-----------------------------------Crea la carpeta
        direccion = os.path.join(carpeta_imagenes, nombre)

    with open(direccion, mode="wb") as imagen:
        imagen.write(respuesta.content)
    print(f"{nombre} descargada correctamente.")


def descargar_imagenes(urls):
    """
    Descarga las imagenes en hilos
    Arguments:
        (urls)str Las url de las imagenes que va a descargar
    returns:
        (archivo_imagen)str Devuelve todos los nombres de las imagenes
    """
    archivo_imagen = []

    hilos = []
    for asd, URL in enumerate(urls): #descarga con hilos las imagenes y las enumera
        nombre_imagen = f"imagen_{asd}.jpg"
        hilo = threading.Thread(target=request, args=(URL, nombre_imagen))
        hilos.append(hilo)
        hilo.start()
        archivo_imagen.append(nombre_imagen)
    for hilo in hilos:
          hilo.join()

    return archivo_imagen
