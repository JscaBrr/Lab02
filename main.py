from dictionary import Dictionary
from translator import Translator

d = Dictionary("dictionary.txt")
t = Translator(d)

while(True):
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