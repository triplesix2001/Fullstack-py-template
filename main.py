import eel
import sys
import ctypes
import os

# Called by script.js, exposing my_python_func
@eel.expose
def my_python_function():
    print("Button clicked!")

# Init logic
def main():
    eel.init("web")
    '''Function to be run as admin'''
    
    eel.start("WindowsStuff.html", port=666, size=(1366, 768))


# Checks and asks for admin
if ctypes.windll.shell32.IsUserAnAdmin():
    main()
else:
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, sys.argv[0], None, 1)
