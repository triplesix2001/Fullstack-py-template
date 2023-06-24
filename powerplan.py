import subprocess

def main():
    def get_active_power_plan():
        try:
            # Execute the powercfg command to get the active power plan
            result = subprocess.run(['powercfg', '-getactivescheme'], capture_output=True, text=True, check=True)

            # Extract the power plan GUID from the command output
            output_lines = result.stdout.strip().split('\n')
            guid_line = output_lines[-1]
            guid_start_index = guid_line.find(':') + 2
            guid = guid_line[guid_start_index:].split()[0]  # Remove the power plan name

            return guid
        except subprocess.CalledProcessError:
            print("Error: Failed to retrieve active power plan.")
            return None
        
    def duplicate_power_plan(source_guid, new_guid, plan_name):
        try:
            result = subprocess.run(['powercfg', '-duplicatescheme', source_guid], capture_output=True, text=True, check=True)
            output = result.stdout.strip()

            # Extract the GUID from the output
            guid_start_index = output.find('Power Scheme GUID: ') + len('Power Scheme GUID: ')
            guid_end_index = output.find(' ', guid_start_index)
            extracted_guid = output[guid_start_index:guid_end_index]

            # Rename the duplicated power plan
            subprocess.run(['powercfg', '-changename', extracted_guid, plan_name], capture_output=True, text=True, check=True)

            print("New power plan created with name:", plan_name)
            print("GUID of the new power plan:", extracted_guid)

            return extracted_guid
        except subprocess.CalledProcessError:
            print("Error: Failed to create duplicate power plan.")

    def set_active_plan(guid):
        try:
            subprocess.run(['powercfg', '-setactive', guid], capture_output=True, text=True, check=True)
            print("Active power plan set to:", guid)
        except subprocess.CalledProcessError:
            print("Error: Failed to set active power plan.")

    def modify_plan():
        try:
            subprocess.run(['powercfg', '-hibernate', "off"], capture_output=True, text=True, check=True)
            subprocess.run(['powercfg', '/change', "monitor-timeout-ac", "0"], capture_output=True, text=True, check=True)
            subprocess.run(['powercfg', '/change', "disk-timeout-ac", "0"], capture_output=True, text=True, check=True)
            subprocess.run(['powercfg', '/change', "standby-timeout-ac", "0"], capture_output=True, text=True, check=True)
            subprocess.run(['powercfg', '/change', "hibernate-timeout-ac", "0"], capture_output=True, text=True, check=True)
            subprocess.run('powercfg /SETACVALUEINDEX SCHEME_CURRENT SUB_BUTTONS LIDACTION 0', shell=True, capture_output=True, text=True)
            print("Modified new power plan")
        except subprocess.CalledProcessError:
            print("Error trying to change powerplann")
    # Example usage
    active_power_plan = get_active_power_plan()
    if active_power_plan:
        print("Active Power Plan GUID:", active_power_plan)
        new_guid = duplicate_power_plan(active_power_plan, "aaaaaaaaa-aaaa-aaaa-aaaa-aaaaaaaaaaaa", "No-sleep-AC")
        set_active_plan(new_guid)
        modify_plan()

if __name__ == "__main__":
    main()
