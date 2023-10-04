from contactList import *

if __name__ == "__main__":
	flag = True
	while flag:
		scelta = int(input("--- Menu ---\n[1] - StampaLista\n[2] - Cerca\n[3] - Aggiungi\n[4] - Modifica\n[5] - Rinomina\n[6] - Rimuovi\nInserisci scelta -> "))
		if scelta > 6 or scelta < 1:
			flag = False
			print("Arrivederci\n")
		elif scelta == 1:
			stampaContatti()
		elif scelta == 2:
			cercaContatto()
		elif scelta == 3:
			aggiungiContatto()
		elif scelta == 4:
			modificaContatto()
		elif scelta == 5:
			rinonimaContatto()
		elif scelta == 6:
			rimuoviContatto()

