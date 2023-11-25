# Importo le librerie
from colorama import Fore  # BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE
from colorama import Style  # DIM, NORMAL, BRIGHT, RESET_ALL
from faker import Factory
fake = Factory.create('it_IT')
# Variabili
verde = Fore.GREEN
blul = Fore.LIGHTBLUE_EX  # Colora Rosso e rende il testo brillante
reset = Style.RESET_ALL
# Genera una falsa identità
def id_falso(continua=True):
    print(f"{blul}Dr. Fate è pronta per aiutarti!{reset}")
    if continua:
        print(f"\n-----x-----x-----x-----x-----x-----")
        print(f"{verde}Email: {fake.email()}")
        print(f"Nome E Cognome: {fake.name()}")
        print(f"Indirizzo: {fake.address()}")
        print(f"Stato: Italia{reset}")
        print(f"-----x-----x-----x-----x-----x-----")
        scelta = input("Vuoi generare un'altra identità? (S/N): ")
        if scelta.upper() == "S":
            id_falso()
        elif scelta.upper() == "N":
            id_falso(continua=False)
        else:
            print("Scelta non valida.")

    else:
        print("E' un piacere esserti stato di aiuto!")