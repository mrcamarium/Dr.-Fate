"""
Con il comando VRFY e EXPN è possibile la verifica di indirizzi email residenti sul server di posta.
Dal momento che viene spesso usato per scopi di intrusione e spam, molte società lo disabilitano di
default.
"""
# Importo le librerie
import smtplib, colorama, time, re, sys, socket, email
from email_validator import validate_email
from colorama import Fore #BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE
from colorama import Style #DIM, NORMAL, BRIGHT, RESET_ALL
from faker import Factory
fake = Factory.create('it_IT')
# Variabili
verde = Fore.GREEN
reset = Style.RESET_ALL
blu = Fore.BLUE
rosso = Fore.LIGHTRED_EX #Colora Rosso e rende il testo brillante
opaco = Style.DIM
brillante = Style.BRIGHT
giallo = Fore.YELLOW
#Info
with open('Info/info.txt', encoding='utf8') as f:
     print(blu + f.read() + reset,'\n')
time.sleep(1) #Pausa
#Analisi dei dati di rete
hostname = socket.gethostname()
ipAddress = socket.gethostbyname(hostname)
print(f"Hostname: {hostname}")
print('Il mio indirizzo IP locale è: ', ipAddress,'\n')
time.sleep(2) #Pausa
def verifica_sintassi(email): #Definisco una funzione che controlla la sintassi di un indirizzo email
  regex = "^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+[a-zA-Z0-9-.]+$" #Uso una regex per verificare che l'email abbia il formato corretto
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
\t 3. Genera una falsa identità
\t 4. Estrai Dati Email
\t 5. Exit
""" + reset)
def control(): #Lista azioni
    ctrl = input("Effettua La Scelta: ")
    if ctrl == "1" :
        veremail() #Controllo indirizzo email
    elif ctrl == "2" :
        ipinfo() #Controllo indirizzo IP
    elif ctrl == "3" :
        IDFalso() #Genera una falsa identità
    elif ctrl == "4" :
        mailinfo()
    elif ctrl == "5" :
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
def IDFalso(): #Genera una falsa identità
    print("\n","-----x-----x-----x-----x-----")
    print(verde + "Email: ",fake.email())
    print("Nome E Cognome: ",fake.name())
    print("Indirizzo: ",fake.address())
    print("Stato: Italia" + reset)
    print("-----x-----x-----x-----x-----")
def mailinfo():
	eml = input("Inserisci il percorso del file: ")
	with open(eml, "r") as f:
		msg = email.message_from_file(f)
	headers = email.message_from_string(msg.as_string())
	infomail={
		"message-id":"",
		"spf-record":False,
		"dkim-record":False,
		"dmarc-record":False,
		"spoofed":False,
		"ip-address":"",
		"sender-client":"",
		"spoofed-mail":"",
		"dt":"",
		"content-type":"",
		"subject":""
	}
	for h in headers.items():
		#ID Messaggio
		if h[0].lower()=="message-id":
			infomail["message-id"]=h[1]
		#Server da dove è stata inviata l'email
		if h[0].lower()=="received":
			infomail["sender-client"]=h[1]
		#Autenticazione rilevata dal server di posta
		if h[0].lower()=="authentication-results":
			if(re.search("spf=pass",h[1])):
				infomail["spf-record"]=True;
			if(re.search("dkim=pass",h[1])):
				infomail["dkim-record"]=True
			if(re.search("dmarc=pass",h[1])):
				infomail["dmarc-record"]=True
			if(re.search("does not designate",h[1])):
				infomail["spoofed"]=True
			if(re.search(r"(\d{1,3}\.){3}\d{1,3}", h[1])):
				ip=re.search(r"(\d{1,3}\.){3}\d{1,3}", h[1])
				infomail["ip-address"]=str(ip.group())
		if h[0].lower()=="reply-to":
			infomail["spoofed-mail"]=h[1]
		if h[0].lower()=="date":
			infomail["dt"]=h[1]
		if h[0].lower()=="content-type":
			infomail["content-type"]=h[1]
		if h[0].lower()=="subject":
			infomail["subject"]=h[1]
	print("\n=========================Risultato=========================\n")
	print("[+] ID Messaggio: "+infomail["message-id"])
	if(infomail["spf-record"]):
		print("[+] " + verde + "SPF Records: PASS"+ reset)
	else:
		print("[+] " + rosso + "SPF Records: FAIL" + reset)
	if(infomail["dkim-record"]):
		print("[+] " + verde + "DKIM: PASS" + reset)
	else:
		print("[+] " + rosso + "DKIM: FAIL" + reset)
	if(infomail["dmarc-record"]):
		print("[+] " + verde + "DMARC: PASS" + reset)
	else:
		print("[+] " + rosso + "DMARC: FAIL" + reset)
	if(infomail["spoofed"] and (not infomail["spf-record"]) and (not infomail["dkim-record"]) and (not infomail["dmarc-record"])):
		print("[+] " + rosso + "L'E-mail è contraffatta" + reset)
		print("[+] " + giallo + "E-mail: " + infomail["spoofed-mail"] + reset)
		print("[+] " + giallo + "Indirizzo IP: " + infomail["ip-address"] + reset)
	else:
		print("[+] " + verde + "L'E-mail è autentica" + reset)
		print("[+] " + giallo + "IP-Address: " + infomail["ip-address"] + reset)
	print("[+] Provider: " + infomail["sender-client"])
	print("[+] Tipo di contenuto: " + infomail["content-type"])
	print("[+] Data e Ora: " + infomail["dt"])
	print("[+] Oggetto: " + infomail["subject"]+"\n\n")
while True: #Ricomincia il programma
 menu()
 control()