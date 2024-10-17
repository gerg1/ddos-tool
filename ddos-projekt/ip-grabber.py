import socket
import os
import sys
import time
import subprocess
from colorama import init, Fore, Style


init()

def get_ip(domain):
    try:
        ip = socket.gethostbyname(domain)
        print(Fore.GREEN + f"the IP of {domain} is {ip}")
    except socket.gaierror as e:
        print(Fore.RED + f"error getting IP address: {e}")

def main():
    domain = input("enter domain (without prefix and -> / <- suffix): ")
    get_ip(domain)
    print("returning to menu in 5 seconds...")
    time.sleep(5)
    os.system('cls')
    script_dir = os.path.dirname(os.path.abspath(__file__))  
    menu_path = os.path.join(script_dir, 'menu.exe')
    subprocess.Popen(['python', menu_path])  
    sys.exit()

if __name__ == "__main__":
    main()
