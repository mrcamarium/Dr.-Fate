# Importo le librerie
import email
import os.path
import re
import requests
import smtplib
import socket
import sys
import time
import webbrowser
import vera_mail
from colorama import Fore  # BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE
from colorama import Style  # DIM, NORMAL, BRIGHT, RESET_ALL
from email_validator import validate_email
from faker import Factory
fake = Factory.create('it_IT')
# Variabili
reset = Style.RESET_ALL
blul = Fore.LIGHTBLUE_EX  # Colora Blu e rende il testo brillante
# Verifico IP
def ipinfo(continua=True):
    print(f"{blul}Dr. Fato è pronto per localizare l'IP{reset}")
    if continua:
        new = 2
        url = "https://ipinfo.io/"
        term = input("Inserisci Indirizzo IP: ")
        webbrowser.open(f"{url}{term}", new=new)
        scelta = input("Vuoi controllare un altro IP? (S/N): ")
        if scelta.upper() == "S":
            ipinfo()
        elif scelta.upper() == "N":
            ipinfo(continua=False)
        else:
            print("Scelta non valida.")
    else:
        print("E' un piacere esserti stato di aiuto!")