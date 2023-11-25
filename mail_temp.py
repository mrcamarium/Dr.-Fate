import requests
import random
import string
import time
import re
from bs4 import BeautifulSoup
from colorama import Fore  # BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE
from colorama import Style  # DIM, NORMAL, BRIGHT, RESET_ALL
# Variabili
reset = Style.RESET_ALL
giallo = Fore.YELLOW
def getActiveDomains():
    domains = requests.get("https://www.1secmail.com/api/v1/?action=getDomainList")
    if domains.status_code == 200:
        domains = domains.json()
    return domains
def createMailbox(domains):
    login = ""
    while len(login) < 16:
        digit = random.randint(0, 9)
        letter = random.choice(string.ascii_lowercase)
        choice = random.randint(1, 2)
        if choice == 1:
            login += str(digit)
        elif choice == 2:
            login = login + letter
    domain = domains[random.randint(0, len(domains))]
    print(f"\nIl tuo indirizzo email temporaneo è: {login}@{domain}\n")
    return login, domain
def createNewMailbox():
    domains = getActiveDomains()
    address = createMailbox(domains)
    getMail(address[0], address[1])
def getMail(login, domain):
    while True:
        print(f"\nControllo posta per {login}@{domain} ...")
        try:
            mailbox = requests.get(f"https://www.1secmail.com/api/v1/?action=getMessages&login={login}&domain={domain}")
        except:
            print("Errore API, riprovare tra 20 secondi...")
            time.sleep(20)
        if mailbox.status_code == 200:
            mailbox = mailbox.json()
            try:
                if len(str(mailbox[0]['id'])) > 1:
                    emailCount = len(mailbox)
                    print(f"\nC'è {emailCount} e-mail nella tua casella di posta") if emailCount == 1 else print(
                        f"\nC'è {emailCount} e-mail nella tua casella di posta")
                    for email in mailbox:
                        message = requests.get(f"https://www.1secmail.com/api/v1/?action=readMessage&login={login}&domain={domain}&id={email['id']}")
                        if message.status_code == 200:
                            message = message.json()
                            message = message['body']
                            message = BeautifulSoup(
                                message, 'html.parser').get_text(separator="\n")
                        else:
                            message = "Error"
                        print(f"\nDa: {email['from']}")
                        print(f"Oggetto: {email['subject']}")
                        print(f"Ora: {email['date']}")
                        print(f"Messaggio: \n\n{message}\n----------")
                    print("\nAggiornamento ogni 20 secondi...")
                else:
                    print("Casella di posta vuota, aggiornamento automatico ogni 20 secondi...")
            except:
                print("Casella di posta vuota, aggiornamento automatico ogni 20 secondi...")
            time.sleep(20)
        risposta = input("Vuoi continuare a controllare la posta? (S/N) ")
        if risposta.lower() == "n":
            break
    print("Hai terminato il controllo della posta")

def readExistingMailbox():
    print("\nAttenzione: le caselle di posta sono temporanee, le email vengono cancellate periodicamente\n")
    address = input("Inserisci l'indirizzo email:")
    domains = getActiveDomains()
    r = r'[^@]+@[^@]+\.[^@]+'
    if re.fullmatch(r, address):
        address = address.split("@")
        for domain in domains:
            if address[1] == domain:
                getMail(address[0], address[1])
        print("Email non valida")
        homeMenu()
    else:
        print("Email non valida")
        homeMenu()
def homeMenu():
    print(giallo + """
    \t Menu:
    \t 1. Crea una casella di posta temporanea
    \t 2. Controlla la casella di posta che hai creato
    \t 3. Ritorna al Menu principale
    """ + reset)
    ctrl = input("Effettua La Scelta: ")
    if ctrl == "1":
        createNewMailbox()  # Crea una casella di posta temporanea
    elif ctrl == "2":
        readExistingMailbox()  # Controlla la casella di posta che hai creato
    elif ctrl == "3":
        return  # Ritorna al Menu principale
    else:
        print(rosso + "Scelta Errata" + reset)