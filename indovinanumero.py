import random

def gioco_indovina_numero():
    numero_da_indovinare = random.randint(1, 100)
    tentativi = 0

    print("Ciao! Prova ad indovinare il numero compreso tra 1 e 100.")

    while True:
        tentativo = int(input("Inserisci il tuo tentativo: "))
        tentativi += 1

        if tentativo < numero_da_indovinare:
            print("Il numero da indovinare è maggiore.")
        elif tentativo > numero_da_indovinare:
            print("Il numero da indovinare è minore.")
        else:
            print(f"Complimenti! Hai indovinato il numero {numero_da_indovinare} in {tentativi} tentativi.")
            break

if __name__ == "__main__":
    gioco_indovina_numero()
