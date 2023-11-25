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
from colorama import Fore  # BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE
from colorama import Style  # DIM, NORMAL, BRIGHT, RESET_ALL
from email_validator import validate_email
from faker import Factory
fake = Factory.create('it_IT')
# Variabili
verde = Fore.GREEN
reset = Style.RESET_ALL
blul = Fore.LIGHTBLUE_EX  # Colora Blu e rende il testo brillante
rosso = Fore.LIGHTRED_EX  # Colora Rosso e rende il testo brillante
giallo = Fore.YELLOW
def verifica_sintassi(mail):
    regex = "^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+[a-zA-Z0-9-.]+$"
    return bool(re.match(regex, mail))
def verifica_dominio(mail):
    try:
        return validate_email(mail)
    except:
        return False
def verifica_esistenza(mail):
    nome, dominio = mail.split("@")
    smtp = smtplib.SMTP()
    try:
        smtp.connect("mail." + dominio)
        smtp.helo()
        codice, messaggio = smtp.vrfy(nome)
        smtp.quit()
        print(messaggio)
        return codice == 250
    except:
        return False
def veremail(continua=True):
    print(f"{blul}Dr. Fato è pronta per verificare l'Email{reset}")
    if continua:
        mail = input("Inserisci l'indirizzo email da verificare: ")
        print("Controllo in corso...")
        if verifica_sintassi(mail):
            print(f"{verde}L'email ha una sintassi valida.{reset}")
            if verifica_dominio(mail):
                print(f"{verde}'Dominio Valido'{reset}")
                if verifica_esistenza(mail):
                    print(f"{verde}L'email esiste ed è funzionante.{reset}")
                else:
                    print(
                        f"{rosso}L'email non esiste o non è funzionante.{giallo}  (Alcuni disabilitano VRFY e EXPN){reset}")
            else:
                print(f"{rosso}Dominio Inesistente{reset}")
        else:
            print(f"{rosso}L'email ha una sintassi non valida.{reset}")
        scelta = input("Vuoi controllare un altro indirizzo? (S/N): ")
        if scelta.upper() == "S":
            veremail()
        elif scelta.upper() == "N":
            veremail(continua=False)
        else:
            print("Scelta non valida.")
    else:
        print("E' un piacere esserti stato di aiuto!")