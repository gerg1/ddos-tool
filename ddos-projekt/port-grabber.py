import socket
import threading
import time
import subprocess
import os
import sys
from colorama import init, Fore, Style

# Initialisieren von colorama
init()

print(Fore.LIGHTGREEN_EX + "NOTE: scanning open ports is an intrusion into network security. Be aware of what you're doing!\nAlso make sure you didn't copy any space, else the grapper won't work.")
print(Fore.LIGHTGREEN_EX + "------------------------------------------------------------------------------------------------------------------------")
print(Fore.WHITE + " ")

def read_end_port(file_path):
    try:
        with open(file_path, 'r') as file:
            end_port = int(file.read().strip())
            return end_port
    except FileNotFoundError:
        print(Fore.RED + f"{file_path} not found.")
        return None
    except ValueError:
        print(Fore.RED + f"Invalid value in {file_path}.")
        return None

def scan_port(ip, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((ip, port))
        if result == 0:
            print(Fore.GREEN + f"Port {port} is open")
        else:
            print(Fore.RED + f"Port {port} is closed")
        sock.close()
    except Exception as e:
        print(Fore.RED + f"Error: {e}")

def main():
    ip = input("Enter target IP: ")
    start_port = 1
    file_path = 'config.txt'
    end_port = read_end_port(file_path)

    if end_port is None:
        print(Fore.RED + "Portscan aborted due to error in config file.")
        return
    
    print("Scanning ports...")
    for port in range(start_port, end_port + 1):
        scan_port(ip, port)
    
    print("Portscan complete")
    print("Returning to menu in 5 seconds...")
    time.sleep(5)
    os.system('cls')
    script_dir = os.path.dirname(os.path.abspath(__file__))
    menu_path = os.path.join(script_dir, 'menu.exe')
    subprocess.Popen(['python', menu_path])
    sys.exit()

if __name__ == "__main__":
    main()
