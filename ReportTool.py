import requests, os, time
from requests.sessions import session
import colorama
from colorama import Fore
colorama.init()

session = requests.session()

print(Fore.MAGENTA + """
██████╗ ███████╗██████╗  █████╗ ██████╗ ████████╗████████╗ █████╗ █████╗  ██╗        ██████╗ ██╗   ██╗
██╔══██╗██╔════╝██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝╚══██╔══╝██╔══██╗██╔══██╗██║        ██╔══██╗╚██╗ ██╔╝
██████╔╝█████╗  ██████╔╝██║  ██║██████╔╝   ██║      ██║   ██║  ██║██║  ██║██║        ██████╔╝ ╚████╔╝
██╔══██╗██╔══╝  ██╔═══╝ ██║  ██║██╔══██╗   ██║      ██║   ██║  ██║██║  ██║██║        ██╔═══╝   ╚██╔╝
██║  ██║███████╗██║     ╚█████╔╝██║  ██║   ██║      ██║   ╚█████╔╝╚█████╔╝███████╗██╗██║        ██║
╚═╝  ╚═╝╚══════╝╚═╝      ╚════╝ ╚═╝  ╚═╝   ╚═╝      ╚═╝    ╚════╝  ╚════╝ ╚══════╝╚═╝╚═╝        ╚═╝
""")
print("Tip: Toggle a vpn before using this, before getting ip banned by tiktok.")
time.sleep(2)
os.system("cls")


print("Welcome, " + os.getlogin() + ".")

x = input('Enter Target url: ')

os.system("cls")


while True:
    Post = session.post(x)
    print(" Successfuly Sent Report " + Post.text)

    time.sleep(2)
input()