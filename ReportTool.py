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

x = input('Enter Url: ')
print("Success!")
time.sleep(2)

os.system("cls")


while True:
    Post = session.post(x)
    print(" Successfuly Sent Report " + Post.text)
input()