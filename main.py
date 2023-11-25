# Importo le librerie
import requests
import socket
import sys
import time
import vera_mail
import my_ip
import identy
import anonimo
import mail_temp
import info_mail
from colorama import Fore  # BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE
from colorama import Style  # DIM, NORMAL, BRIGHT, RESET_ALL
# Variabili
verde = Fore.GREEN
reset = Style.RESET_ALL
blu = Fore.BLUE
rosso = Fore.LIGHTRED_EX  # Colora Rosso e rende il testo brillante
opaco = Style.DIM
brillante = Style.BRIGHT
giallo = Fore.YELLOW
# Banner
print (f"""{blu}
░▒█▀▀▄░█▀▀▄░░░░░░▒█▀▀▀░█▀▀▄░▀█▀░▄▀▀▄
░▒█░▒█░█▄▄▀░▄▄░░░▒█▀▀░░█▄▄█░░█░░█░░█
░▒█▄▄█░▀░▀▀░▀▀░░░▒█░░░░▀░░▀░░▀░░░▀▀░

             Version 2.3.9
          Autore: Mr. Camarium
            Canale Youtube
              mrcamarium{reset}""")
time.sleep(1)  # Pausa
# Analisi dei dati di rete
hostname = socket.gethostname()
ipAddress = socket.gethostbyname(hostname)
publicIp = requests.get('https://checkip.amazonaws.com').text.strip()
print(f"Hostname: {hostname}")
print("IP locale: ", ipAddress)
print("IP pubblico: ", publicIp, '\n')
time.sleep(1)  # Pausa
# Menu
def menu():
    print(giallo + """
    \t Menu:
    \t 1. Verifica Indirizzo Email
    \t 2. Verifica Indirizzo IP
    \t 3. Genera una falsa identità
    \t 4. Invia Email Anonima
    \t 5. Genera Una Email Temporanea
    \t 6. Estrai Dati Email
    \t 7. Exit
    """ + reset)
# Lista azioni
def control():
    ctrl = input("Effettua La Scelta: ")
    if ctrl == "1":
        vera_mail.veremail()  # Controllo indirizzo email
    elif ctrl == "2":
        my_ip.ipinfo()  # Controllo indirizzo IP
    elif ctrl == "3":
        identy.id_falso()  # Genera una falsa identità
    elif ctrl == "4":
        anonimo.anon_mail()  # Invia Email Anonima
    elif ctrl == "5":
        mail_temp.homeMenu() # Genera Una Email Temporanea
    elif ctrl == "6":
        info_mail.mailinfo()  # Esamina il soregnte di una email
    elif ctrl == "7":
        sys.exit()
    else:
        print(rosso + "Scelta Errata" + reset)
# Ricomincia il programma
while True:
    menu()
    control()