import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import os
import shutil

def enviar_correo(archivos, destinatario, usuario):
    """
    Envia las imagenes por correo electronico
    @param archivos Los archivos que se van a enviar por correo
    @param destinatario El correo al cual se van a enviar las imagenes
    @param usuario El nombre del usuario
    @returns
    """

    context = ssl.create_default_context()
    mensaje = MIMEMultipart("alternative")
    mensaje["Subject"] = "Saludos desde Python"
    mensaje["From"] = "Mario Montero Badilla <estebanmonba@gmail.com >"
    mensaje["To"] = destinatario #--------------------------------------Ingresa el correo del usuario

    ruta_plantilla = "plantilla_saludo.html" #--------------------------Localiza la plantilla
    with open(ruta_plantilla, mode="r", encoding="utf-8") as plantilla:
        html = plantilla.read() #---------------------------------------La lee y la asigna a una variable

    imagen = "<p>" 
    for archivo in archivos: #------------------------------------------ingresa los nombres de las imagenes a un codigo html
        x = f"""
            <ul>
                <li>{archivo}</li>
            </ul>
        """
        imagen += x
    imagen += "</p>" #------------------------------------------cierra el codigo

    html = html % { #-------------------------------------------ingresa el usuario y el codigo previamente escritos
        "nombre_persona": usuario,
        "Imagenes": imagen,
    }
    
    cuerpo_html = MIMEText(html, "html") #----------------------define el texto como html
    mensaje.attach(cuerpo_html) #-------------------------------agrega el texto al contenido del correo

    for ruta_archivo in archivos: #-----------------------------adjunta las imagenes
        ruta_archivo = "img/" + ruta_archivo#-------------------asigna la ruta del archivo 
        adjunto_imagen = MIMEBase("application", "octet-stream")
        with open(ruta_archivo, mode="rb") as archivos:
            adjunto_imagen.set_payload(archivos.read())

        encoders.encode_base64(adjunto_imagen)

        adjunto_imagen.add_header(
            "Content-Disposition",
            f"attachment; filename={ruta_archivo}",
        )
        mensaje.attach(adjunto_imagen)#-------------------Adjunta la imagen

    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as conexion: #conecta con el servidor
        
        conexion.login("estebanmonba@gmail.com", "ygewtolrblpminbx")#-----------inicia sesion
        respuesta = conexion.sendmail( #----------------------------------------envia el correo
            "estebanmonba@gmail.com",
            destinatario,#------------------------------------------------------Ingresa el correo del usuario
            mensaje.as_string()
            )
    print(respuesta)


def eliminar_archivos():
    Borrar = os.getcwd()
    Borrar = Borrar + "\img"#------------------------------Localiza la carpeta
    try:
        shutil.rmtree(Borrar)#-----------------------------Borra los archivos
        print("Archivos eliminados")
    except OSError as error:
        print(f"error al eliminar los archivos: {error}")

    


