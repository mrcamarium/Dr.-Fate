"""
Con il comando VRFY e EXPN è possibile la verifica di indirizzi email residenti sul server di posta.
Dal momento che viene spesso usato per scopi di intrusione e spam, molte società lo disabilitano di
default.
"""
# Importo le librerie
import smtplib, colorama, time, re, sys, socket
from email_validator import validate_email
from colorama import Fore #BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE
from colorama import Style #DIM, NORMAL, BRIGHT, RESET_ALL
# Variabili
verde = Fore.GREEN
reset = Style.RESET_ALL
blu = Fore.BLUE
rosso = Fore.LIGHTRED_EX #Colora Rosso e rende il testo brillante
opaco = Style.DIM
brillante = Style.BRIGHT
giallo = Fore.YELLOW
#Info
print(blu + brillante + "Version 1.7.4" + reset)
print(blu + opaco + "Codice by - Mr. Camarium")
print(blu + "Youtube - mrcamarium" + reset, '\n')
hostname = socket.gethostname()
ipAddress = socket.gethostbyname(hostname)
print(f"Hostname: {hostname}")
print('Il mio indirizzo IP è: ', ipAddress,'\n')
time.sleep(1) #Pausa
def verifica_sintassi(email): #Definisco una funzione che controlla la sintassi di un indirizzo email
  regex = "^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$" #Uso una regex per verificare che l'email abbia il formato corretto
  return bool(re.match(regex, email)) #Restituisco True se l'email è valida, False altrimenti
def verifica_dominio(email): #Definisco una funzione che controlla l'esistenza del dominio di un indirizzo email
        try:
         return validate_email(email)
        except:
         return False #Se lo stato è diverso, restituisco False
def verifica_esistenza(email): #Definisco una funzione che controlla l'esistenza di un indirizzo email
  nome, dominio = email.split("@") #Divido l'email in nome utente e dominio
  smtp = smtplib.SMTP() #Creo un oggetto SMTP per connettermi al server del dominio
  try:
    smtp.connect("mail." + dominio) #Provo a connettermi al server e a inviare un comando HELO
    smtp.helo()
    codice, messaggio = smtp.vrfy(nome) #Provo a inviare un comando VRFY con il nome utente
    smtp.quit() #Chiudo la connessione
    return codice == 250 #Restituisco True se il codice è 250 (OK)
  except:
    return False #Se il codice è diverso, restituisco False
def menu(): #Menu
    print(giallo + """
\t 1. Verifica Indirizzo Email
\t 2. Verifica Indirizzo IP
\t 3. Null
\t 4. Null
\t 5. Null
\t 6. Null
\t 7. Exit
""" + reset)
def control(): #Lista azioni
    ctrl = input("Effettua La Scelta: ")
    if ctrl == "1" :
        veremail() #Controllo indirizzo email
    elif ctrl == "2" :
        ipinfo() #Controllo indirizzo IP
    elif ctrl == "3" :
        veremail()
    elif ctrl == "7" :
        sys.exit()
    else :
        print(rosso + "Scelta Errata" + reset)    
def veremail(): #Verifico Email
   email = input("Inserisci l'indirizzo email da verificare: ") #Chiedo all'utente di inserire un indirizzo email da verificare
   print("Controllo in corso...")
   if verifica_sintassi(email): #Controllo la sintassi dell'email
    print(verde + "L'email ha una sintassi valida.")
    if verifica_dominio(email): #Controllo il dominio dell'email
     print(verde + 'Dominio Valido' + reset)
     if verifica_esistenza(email): #Controllo l'esistenza dell'email
      print(verde + "L'email esiste ed è funzionante." + reset)
     else:
      print(rosso + "L'email non esiste o non è funzionante. " + giallo + "(PS alcuni provider disabilitano VRFY e EXPN)" + reset)
    else:
     print(rosso + "Dominio Inesistente" + reset)
   else:
    print(rosso + "L'email ha una sintassi non valida." + reset)
def ipinfo(): #Verifico IP
    import webbrowser
    new = 2
    url = ("https://ipinfo.io/")
    term = input("Inserisci Indirizzo IP: ")
    webbrowser.open(url+term,new=new)
while True: #Ricomincia il programma
 menu()
 control()