import translator
import dictionary

filename = input("nome file txt:")
t = translator.Translator()
t.loadDictionary(filename)

while(True): #ciclo infinito che consente all'utente di interagire con il programma in un ambiente menu-driven, fino a quando l'utente non sceglie di uscire.
    t.printMenu()

    #t.loadDictionary("dictionary.txt")

    try:
        i = int(input("\n Scegli un'opzione:"))

        if i == 1:
            parola = input("Inserisci la parola e la traduzione (es. 'alieno extraterrestre'): ")
            t.handleAdd(parola)
        elif i == 2:
            parola = input("Inserisci la parola da tradurre: ")
            t.handleTranslate(parola)
        elif i == 3:
            parola = input("Inserisci la parola con '?': ")
            t.handleWildCard(parola)
        elif i == 4:
            print("Chiusura del programma...")
            break
        else:
            print("Opzione non valida")

    except ValueError:
        print("Errore: Devi inserire un numero valido.")

