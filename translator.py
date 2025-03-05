import os
import re
from dictionary import Dictionary

class Translator:

    def __init__(self):
        self.dictionary = Dictionary()

    def printMenu(self):
        print("\nMenu:")
        print("1. Aggiungi una nuova parola")
        print("2. Cerca una traduzione")
        print("3. Cerca con wildcard")
        print("4. Esci")

    def loadDictionary(self, filename):
        self.dictionary = Dictionary(filename)
        if not os.path.exists(filename):
            print(f"Errore: Il file '{filename}' non esiste.")
            return
        try:
            with open(filename, "r", encoding="utf-8") as file:
                for line in file:
                    if not re.match("^[a-zA-Zà-öÀ-Ö ]+$", line):
                        print("Errore: L'input può contenere solo lettere e spazi.")
                        return
                    line = line.lower()
                    parts = line.strip().split(" ", 1)
                    if len(parts) == 2:
                        self.dictionary.addWord(parts[0], parts[1])
            print(self.dictionary.words)
            #print("Dizionario caricato")
            #print(self.dictionary)
        except IOError:
            print(f"Errore: Problema nell'apertura o lettura del file '{filename}'.")

    def handleAdd(self, entry):
        #entry is a tuple '<parola aliena><traduzione1 traduzione2>'
        if not re.match("^[a-zA-Z ]+$", entry):
            print("Errore: L'input può contenere solo lettere e spazi.")
            return
        entry = entry.lower()
        parts = entry.split(" ",1)
        print(parts[1])
        if len(parts) < 2:
            print("Errore: formato non valido. Formato richiesto: '<parola aliena> <traduzione1 traduzione2>'")
        self.dictionary.addWord(parts[0], parts[1])

    def handleTranslate(self, query):
        # query is a string <parola_aliena>
        query = query.lower()
        try:
            traduzione = self.dictionary.words[query]
            if len(traduzione) == 1:
                print(f"Traduzion* di {query}: {traduzione[0]}")
            else:
                print(f"Traduzion* di {query}: " + " - ".join(traduzione))

        except KeyError:
            print(f"Errore: La parola '{query}' non è presente nel dizionario.")

    def handleWildCard(self,query):
        # query is a string with a ? --> <par?la_aliena>
        query = query.lower()
        pattern = query.replace("?", ".")
        #matched_words = [word for word in self.dictionary if re.match(pattern, word)]
        matched_words = []
        for word in self.dictionary.words:
            if re.match(pattern, word):
                matched_words.append(word)
        if matched_words:
            print(f"Corrispondenze: {', '.join(matched_words)}")
            for w in matched_words:
                self.handleTranslate(w)
        else:
            print(f"Nessuna parola corrisponde alla query '{query}'.")





