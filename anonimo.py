# Importo le librerie
import smtplib
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
# Email Anonima
def credenziali():
    with open("credenziali.txt", "r") as file:
        username = file.readline().strip()
        password = file.readline().strip()
        return username, password
# Email Anonima
def anon_mail():
    username, password = credenziali()
    oggetto = "Subject: Urgente! da leggere subito!\n\n"
    contenuto = "connettiti al Server che è meglio..."
    messaggio = oggetto + contenuto
    try:
        mail = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        mail.login(username, password)
        mail.sendmail(username, username, messaggio)
        mail.quit()
        print("Email inviata con successo!")
    except smtplib.SMTPException as e:
        print("Errore durante l'invio della email:", e.args[1].decode())