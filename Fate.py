"""
Installa email-validator
pip install email-validator
"""
import colorama, time
from email_validator import validate_email
from colorama import Fore #BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE
from colorama import Style #DIM, NORMAL, BRIGHT, RESET_ALL
# Variabili
verde = Fore.GREEN
reset = Style.RESET_ALL
blu = Fore.BLUE
rosso = Fore.LIGHTRED_EX # Colora Rosso e rende il testo brillante
opaco = Style.DIM
brillante = Style.BRIGHT
# Info
print(blu + brillante + "Version 0.1.3" + reset)
print(blu + opaco + "Codice by - Mr. Camarium")
print(blu + "Youtube - mrcamarium" + reset)
# Pausa
time.sleep(1)
#Verifica validità dominio dell'indirizzo e-mail
def verifica_Dominio():
    while True:
        email = input("Inserisci Email da controllare: ")
        try:
            validate_email(email)
            print(verde + 'Dominio Valido' + reset)
        except:
            print(rosso + "Dominio Non Valido" + reset)
        scelta = input("Vuoi verificare un altro indirizzo? Scegliere y/n > ")
        if (scelta == 'n'):
            print("Uscita in corso...")
            # Pausa
            time.sleep(1)
            break
#main
verifica_Dominio()