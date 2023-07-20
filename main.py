import sys
import ctypes
import os
import subprocess
import traceback
import winreg
import dearpygui.dearpygui as dpg
import dearpygui.demo as demo


def disable_telemetry():
    try:
        key_path = r"SOFTWARE\Policies\Microsoft\Windows\DataCollection"
        with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, key_path, 0, winreg.KEY_ALL_ACCESS) as reg_key:
            winreg.SetValueEx(reg_key, "AllowTelemetry", 0, winreg.REG_DWORD, 0)
        return "success"
    except Exception as e:
        traceback.print_exc()
        return str(e)

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


def disable_sleep_lid_close():
    try:
        subprocess.run('powercfg /SETACVALUEINDEX SCHEME_CURRENT SUB_BUTTONS LIDACTION 0', shell=True, capture_output=True, text=True)
        subprocess.run('powercfg /setActive scheme_current', shell=True, capture_output=True, text=True)
        return "success"
    except Exception as e:
        return str(e)

def windows_cracker():
    try:
        subprocess.Popen(['start', '/wait', 'powershell.exe', 'irm https://massgrave.dev/get | iex'], shell=True)
        return "success"
    except Exception as e:
        return str(e)

def disable_win11():
    try:
        subprocess.run('reg add HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\WindowsUpdate /v TargetReleaseversion /t REG_DWORD /d 1', shell=True, capture_output=True, text=True)
        subprocess.run('reg add HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\WindowsUpdate /v TargetReleaseversionInfo /t REG_SZ /d 21H2', shell=True, capture_output=True, text=True)
        subprocess.run('gpupdate /force', shell=True, capture_output=True, text=True)
        return "success"
    except Exception as e:
        return str(e)
    

checked_checkboxes = []

def checkbox_callback(sender, app_data):
    checkbox_label = dpg.get_item_label(sender)
    checkbox_value = app_data
    if checkbox_value:
        checked_checkboxes.append(checkbox_label)
    else:
        checked_checkboxes.remove(checkbox_label)

def run_button_callback(sender, app_data):
    print("Checked checkboxes:")
    for checkbox_label in checked_checkboxes:
        print(checkbox_label)

    # Check specific options and perform actions accordingly
    if "Option 1" in checked_checkboxes:
        print("Option 1 is checked. Performing action for Option 1.")
        # Add your action for Option 1 here
        pass

    if "Option 2" in checked_checkboxes:
        print("Option 2 is checked. Performing action for Option 2.")
        # Add your action for Option 2 here
        pass

    if "Option 3" in checked_checkboxes:
        print("Option 3 is checked. Performing action for Option 3.")
        # Add your action for Option 3 here
        pass

    if "Option 4" in checked_checkboxes:
        print("Option 4 is checked. Performing action for Option 4.")
        # Add your action for Option 4 here
        pass

def main():
    dpg.create_context()

    dpg.set_global_font_scale(1.25)

    with dpg.window(tag="Primary Window"):
        dpg.add_text("Prebens toolbox")
        dpg.add_separator()

        dpg.add_spacing(count=3)
        with dpg.collapsing_header(label="Windows"):

            with dpg.tree_node(label="Battery"):
                # Create a bunch of checkboxes with labels
                checkbox_labels = ["Disable sleep on lid close", "Disable all sleep"]
                for label in checkbox_labels:
                    # Add the checkbox
                    dpg.add_checkbox(label=label, callback=checkbox_callback)

            with dpg.tree_node(label='Updates'):
                checkbox_labels = ["Disable Windows 11", "Disable automatic updates"]
                for label in checkbox_labels:
                    # Add the checkbox
                    dpg.add_checkbox(label=label, callback=checkbox_callback)

            with dpg.tree_node(label='Etc'):
                checkbox_labels = ["Windows / Office cracker", "Disable telemetry", "Install & setup Rustdesk"]
                for label in checkbox_labels:
                    # Add the checkbox
                    dpg.add_checkbox(label=label, callback=checkbox_callback)

        dpg.add_spacing(count=1)
        dpg.add_separator()
        dpg.add_spacing(count=1)

        # Add the "Run" button and its callback
        dpg.add_button(label="Run", callback=run_button_callback)

    dpg.create_viewport(title='Prebens toolbox', width=800, height=600, resizable=False)
    dpg.setup_dearpygui()
    dpg.show_viewport()
    dpg.set_primary_window("Primary Window", True)
    dpg.start_dearpygui()
    dpg.destroy_context()

# Checks and asks for admin
if ctypes.windll.shell32.IsUserAnAdmin():
    main()
else:
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, sys.argv[0], None, 1)