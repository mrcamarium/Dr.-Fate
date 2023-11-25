# Importo le librerie
import re
import email
import os.path
from colorama import Fore  # BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE
from colorama import Style  # DIM, NORMAL, BRIGHT, RESET_ALL
from email_validator import validate_email
from faker import Factory
fake = Factory.create('it_IT')
# Variabili
verde = Fore.GREEN
reset = Style.RESET_ALL
rosso = Fore.LIGHTRED_EX  # Colora Rosso e rende il testo brillante
giallo = Fore.YELLOW
blul = Fore.LIGHTBLUE_EX  # Colora Rosso e rende il testo brillante
# Esamina il sorgente di una email
def mailinfo(continua=True):
    print(f"{blul}Dr. Fato è qui per analizare l'email{reset}")
    if continua:
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
        scelta = input("Vuoi controllare un altra Email? (S/N): ")
        if scelta.upper() == "S":
            mailinfo()
        elif scelta.upper() == "N":
            mailinfo(continua=False)
        else:
            print("Scelta non valida.")
    else:
        print("E' un piacere esserti stato di aiuto!")