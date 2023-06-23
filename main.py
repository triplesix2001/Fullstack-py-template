import eel
import sys
import ctypes
import os
import subprocess
import traceback

# Called by script.js, exposing my_python_func
@eel.expose
def my_python_function():
    print("Button clicked!")

# Exposed function
@eel.expose
def disable_sleep():
    try:
        # Command to set monitor timeout on AC power
        subprocess.run('powercfg /Change monitor-timeout-ac 60', shell=True, capture_output=True, text=True)
        # Command to set monitor timeout on DC power
        subprocess.run('powercfg /Change monitor-timeout-dc 0', shell=True, capture_output=True, text=True)
        # Command to set standby timeout on AC power
        subprocess.run('powercfg /Change standby-timeout-ac 0', shell=True, capture_output=True, text=True)
        # Command to set standby timeout on DC power
        subprocess.run('powercfg /Change standby-timeout-dc 0', shell=True, capture_output=True, text=True)
        subprocess.run('powercfg /setActive scheme_current', shell=True, capture_output=True, text=True)
        return "success"
    except Exception as e:
        traceback.print_exc()  # Print the exception traceback for debugging
        return str(e)


@eel.expose
def disable_sleep_lid_close():
    try:
        subprocess.run('powercfg /SETACVALUEINDEX SCHEME_CURRENT SUB_BUTTONS LIDACTION 0', shell=True, capture_output=True, text=True)
        subprocess.run('powercfg /setActive scheme_current', shell=True, capture_output=True, text=True)
        return "success"
    except Exception as e:
        return str(e)


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
