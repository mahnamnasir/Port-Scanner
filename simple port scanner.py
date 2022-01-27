import ipaddress
import nmap
import re
print("**********************************************************************************************")
print(" ▄▄▄▄▄▄▄ ▄▄▄▄▄▄▄ ▄▄▄▄▄▄   ▄▄▄▄▄▄▄    ▄▄▄▄▄▄▄ ▄▄▄▄▄▄▄ ▄▄▄▄▄▄ ▄▄    ▄ ▄▄    ▄ ▄▄▄▄▄▄▄ ▄▄▄▄▄▄    ")
print(" █       █       █   ▄  █ █       █  █       █       █      █  █  █ █  █  █ █       █   ▄  █  ")
print(" █    ▄  █   ▄   █  █ █ █ █▄     ▄█  █  ▄▄▄▄▄█       █  ▄   █   █▄█ █   █▄█ █    ▄▄▄█  █ █ █  ")
print(" █   █▄█ █  █ █  █   █▄▄█▄  █   █    █ █▄▄▄▄▄█     ▄▄█ █▄█  █       █       █   █▄▄▄█   █▄▄█▄ ")
print(" █    ▄▄▄█  █▄█  █    ▄▄  █ █   █    █▄▄▄▄▄  █    █  █      █  ▄    █  ▄    █    ▄▄▄█    ▄▄  █")
print(" █   █   █       █   █  █ █ █   █     ▄▄▄▄▄█ █    █▄▄█  ▄   █ █ █   █ █ █   █   █▄▄▄█   █  █ █")
print(" █▄▄▄█   █▄▄▄▄▄▄▄█▄▄▄█  █▄█ █▄▄▄█    █▄▄▄▄▄▄▄█▄▄▄▄▄▄▄█▄█ █▄▄█▄█  █▄▄█▄█  █▄▄█▄▄▄▄▄▄▄█▄▄▄█  █▄█")
print("**********************************************************************************************")
port_range_pattern = re.compile("([0-9]+)-([0-9]+)")
port_min = 0
port_max = 65535
# ask user for ip address
while True:
    ip_add_ent = input("Enter the ip address you want to scan:  ")
    try:
        ip_add_obj = ipaddress.ip_address(ip_add_ent)
        print("Valid IP address")
        break
    except:
        print("You entered invalid IP address kindly enter again")
while True:
    print("Please enter the range of ports you want to scan in format :<int>-<int>")
    port_range = input("Enter port range :")
    port_range_valid = port_range_pattern.search(port_range.replace(" ",""))
    if port_range_valid:
        port_min = int(port_range_valid.group(1))
        port_max = int(port_range_valid.group(2))
        break
nm = nmap.PortScanner()
for port in range(port_min, port_max + 1):
    try:
        result = nm.scan(ip_add_ent, str(port))
        port_status = (result['scan'][ip_add_ent]['tcp'][port]['state'])
        print(f"Port {port} is {port_status} ")
    except:
        print(f"cannot scan {port}")






