import pyfiglet
from colorama import Fore
import sys
import time
import os
import subprocess



def open_file_and_exit(file_name):
    script_dir = os.path.dirname(os.path.abspath(__file__))  
    file_path = os.path.join(script_dir, file_name)
    subprocess.Popen(['python', file_path])  
    sys.exit()

def portgrabber():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    portgrabber_path = os.path.join(script_dir, 'port-grabber.py')
    try:
        os.startfile(portgrabber_path)  
    except FileNotFoundError:
        print("file not found.")

def ipgrabber():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    ipgrabber_path = os.path.join(script_dir, 'ip-grabber.py')
    try:
        os.startfile(ipgrabber_path)  
    except FileNotFoundError:
        print("file not found.")

def ddosattack():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    ddosattack_path = os.path.join(script_dir, 'ddos.py')
    try:
        os.startfile(ddosattack_path)  
    except FileNotFoundError:
        print("file not found.")

def stop_program():
    print("program will stop in 3s...")
    time.sleep(3)
    sys.exit()

def readme():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    readme_path = os.path.join(script_dir, 'README.txt')
    try:
        os.startfile(readme_path)  
    except FileNotFoundError:
        print("file not found.")


def start():
    print(Fore.LIGHTGREEN_EX + pyfiglet.figlet_format("get DD0Sed"))
    print("------------------------------------------------------by-gerg-----------------------------------------------------------")
    print(Fore.WHITE + " [1]   README.txt \n [2]   port-grabber\n [3]   ip grabber\n [4]   ddos attack\n [5]   stop program")

    auswahl = int(input("enter: "))

    if auswahl == 1:
        readme()

    elif auswahl == 2:
        portgrabber()

    elif auswahl == 3:
        ipgrabber()
    
    elif auswahl == 4:
        ddosattack()

    elif auswahl == 5:
        stop_program()
start()

