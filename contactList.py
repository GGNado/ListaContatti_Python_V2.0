import os

contactList = {
	'primo' : 3668397915
}

def pulisciTerminale():
	#os.system("clear")
	pass

def stampaContatti():
	pulisciTerminale()
	for contatto in contactList:
		print(f"Indice: {contatto} : {contactList[contatto]}")


def cercaContatto(nome: str = "admin"):
	pulisciTerminale()
	flag = False

	if nome == "admin":
		nome = str(input("Chi contatto cercare? "))
	for contatto in contactList:
		if contatto.lower() == nome.lower():
			print("Contatto trovato!")
			flag = True
			return flag

	print("Contatto non esistente")
	return flag

def aggiungiContatto():
	nome = str(input("Come si chiama il contatto? ")).lower()
	flag = cercaContatto(nome)

	if flag:
		print("Non possibile aggiungere")
		return

	num = input("Proseguo con l'aggiunta. Scrivi il numero di telefono: ")
	contactList[nome] = num

def modificaContatto():
	pulisciTerminale()
	nome = input("Quale utente modificare il numero? ")
	flag = cercaContatto(nome)

	if not flag:
		print("Contatto inesistente")
		return

	contactList[nome] = input("Inserisci numero: ")
	pass

def rinonimaContatto():
	pulisciTerminale()

	num = int(input("Inserisci numero da modificare il nome: "))
	for contatto in contactList:
		if contactList[contatto] == num:
			print("Contatto trovato!")
			nome = input("Inserisci nuovo nome: ")
			contactList[nome] = contactList[contatto]
			del contactList[contatto]
			return


def rimuoviContatto():
	pulisciTerminale()
	nome = input("Inserisci nome da eliminare: ").lower()
	flag = cercaContatto(nome)
	if flag:
		print("Proseguo con eliminazione")
		del contactList[nome]
