import imagen
import correo 




def main():
    """
    Codigo principal que inicia todo el programa
    """
    print("Bienvenido al programa.")
    urls = []
    valor = " "
    print("Si ya no desea agregar más imágenes, deje el espacio en blanco.")
    while valor != "":
        valor = str(input("Ingrese la URL de la imagen que desee descargar:")) #pide las urls
        if valor != "":
            urls.append(valor) #------------------------------------------------las une a una lista

    archivos = imagen.descargar_imagenes(urls)

    print("Imágenes descargadas:", archivos)

    destinatario = str(input("Ingrese el correo al que quiere que le lleguen las imagenes: "))#pide el correo para enviar imagenes
    usuario = str(input("Ingrese su nombre: ")) #----------------------------------------------pide el nombre del usuario


    correo.enviar_correo(archivos, destinatario, usuario)

    pregunta = str.upper(input("Desea eliminar las imagenes de su computadora si/no:"))
    if pregunta == "SI":
        correo.eliminar_archivos()
    else:
        print("Adios")
        




if __name__ == "__main__":
     main()