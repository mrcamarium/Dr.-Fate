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
blu = Fore.BLUE
rosso = Fore.LIGHTRED_EX  # Colora Rosso e rende il testo brillante
opaco = Style.DIM
brillante = Style.BRIGHT
giallo = Fore.YELLOW
# Info
with open('gfate.dll', encoding='utf8') as f:
    print(blu + f.read() + reset, '\n')
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
\t 1. Verifica Indirizzo Email
\t 2. Verifica Indirizzo IP
\t 3. Genera una falsa identità
\t 4. Estrai Dati Email
\t 5. Exit
""" + reset)


# Lista azioni
def control():
    ctrl = input("Effettua La Scelta: ")
    if ctrl == "1":
        veremail()  # Controllo indirizzo email
    elif ctrl == "2":
        ipinfo()  # Controllo indirizzo IP
    elif ctrl == "3":
        id_falso()  # Genera una falsa identità
    elif ctrl == "4":
        mailinfo()  # Esamina il soregnte di una email
    elif ctrl == "5":
        sys.exit()
    else:
        print(rosso + "Scelta Errata" + reset)


# Verifico Email
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


def veremail():
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


# Verifico IP
def ipinfo():
    new = 2
    url = "https://ipinfo.io/"
    term = input("Inserisci Indirizzo IP: ")
    webbrowser.open(f"{url}{term}", new=new)


# Genera una falsa identità
def id_falso():
    print(f"\n-----x-----x-----x-----x-----x-----")
    print(f"{verde}Email: {fake.email()}")
    print(f"Nome E Cognome: {fake.name()}")
    print(f"Indirizzo: {fake.address()}")
    print(f"Stato: Italia{reset}")
    print(f"-----x-----x-----x-----x-----x-----")


# Esamina il sorgente di una email
def mailinfo():
    eml = input("Inserisci il percorso del file: ")
    if os.path.isfile(eml):
        print("Controllo in corso...")
    else:
        print(f"{rosso}Il file non esiste.{reset}")
        mailinfo()
    with open(eml, "r") as f1:
        msg = email.message_from_file(f1)
    headers = email.message_from_string(msg.as_string())
    infomail = {
        "message-id": "",
        "spf-record": False,
        "dkim-record": False,
        "dmarc-record": False,
        "spoofed": False,
        "ip-address": "",
        "sender-client": "",
        "spoofed-mail": "",
        "dt": "",
        "content-type": "",
        "subject": ""
    }
    for h in headers.items():
        if h[0].lower() == "message-id":
            infomail["message-id"] = h[1]
        if h[0].lower() == "received":
            infomail["sender-client"] = h[1]
        if h[0].lower() == "authentication-results":
            if re.search("spf=pass", h[1]):
                infomail["spf-record"] = True
            if re.search("dkim=pass", h[1]):
                infomail["dkim-record"] = True
            if re.search("dmarc=pass", h[1]):
                infomail["dmarc-record"] = True
            if re.search("does not designate", h[1]):
                infomail["spoofed"] = True
            if re.search(r"(\d{1,3}\.){3}\d{1,3}", h[1]):
                ip = re.search(r"(\d{1,3}\.){3}\d{1,3}", h[1])
                infomail["ip-address"] = str(ip.group())
        if h[0].lower() == "reply-to":
            infomail["spoofed-mail"] = h[1]
        if h[0].lower() == "date":
            infomail["dt"] = h[1]
        if h[0].lower() == "content-type":
            infomail["content-type"] = h[1]
        if h[0].lower() == "subject":
            infomail["subject"] = h[1]
    result = giallo + "\n==============================Risultato==============================\n" + reset
    result += "[+] ID Messaggio: {}\n".format(infomail["message-id"])
    if infomail["spf-record"]:
        result += "[+] " + verde + "SPF Records: PASS\n" + reset
    else:
        result += "[+] " + rosso + "SPF Records: FAIL\n" + reset
    if infomail["dkim-record"]:
        result += "[+] " + verde + "DKIM: PASS\n" + reset
    else:
        result += "[+] " + rosso + "DKIM: FAIL\n" + reset
    if infomail["dmarc-record"]:
        result += "[+] " + verde + "DMARC: PASS\n" + reset
    else:
        result += "[+] " + rosso + "DMARC: FAIL\n" + reset
    if (infomail["spoofed"] and (not infomail["spf-record"]) and (not infomail["dkim-record"]) and (not infomail[
        "dmarc-record"])):
        result += "[+] " + rosso + "L'E-mail è contraffatta\n" + reset
        result += "[+] E-mail: {}\n".format(infomail["spoofed-mail"])
        result += "[+] " + giallo + "Indirizzo IP: {}\n".format(infomail["ip-address"] + reset)
    else:
        result += "[+] " + verde + "L'E-mail è autentica\n" + reset
        result += "[+] " + giallo + "Indirizzo IP: {}\n".format(infomail["ip-address"] + reset)

    result += "[+] Provider: {}\n".format(infomail["sender-client"])
    result += "[+] Tipo di contenuto: {}\n".format(infomail["content-type"])
    result += "[+] Data e Ora: {}\n".format(infomail["dt"])
    result += "[+] Oggetto: {}\n\n".format(infomail["subject"])
    print(result)


# Ricomincia il programma
while True:
    menu()
    control()
