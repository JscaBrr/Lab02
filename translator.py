import os
import re
from dictionary import Dictionary

class Translator:

    def __init__(self, filename): #translator di
        self.filename = filename
        self.dizionario = Dictionary(filename)

    def printMenu(self):
     print("\nMenu:")
     print("1. Aggiungi una nuova parola")
     print("2. Cerca una traduzione")
     print("3. Cerca con wildcard")
     print("4. Esci")

    def loadDictionary(self, filename):
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
                        self.dizionario.dizionario[parts[0]] = [parts[1].split(" ")]
            print(self.dizionario.dizionario)
            print("Dizionario caricato")
        except IOError:
            print(f"Errore: Problema nell'apertura o lettura del file '{filename}'.")

    def handleAdd(self, entry):
        #entry is a tuple '<parola aliena><traduzione1 traduzione2>'
        if not re.match("^[a-zA-Z ]+$", entry):
            print("Errore: L'input può contenere solo lettere e spazi.")
            return
        entry = entry.lower()
        parts = entry.split(" ", 1)
        if len(parts) < 2:
            print("Errore: formato non valido. Formato richiesto: '<parola aliena> <traduzione1 traduzione2>'")
            return
        traduzioni = parts[1].strip().split(" ")
        if parts[0] in self.dizionario.dizionario:
            for v in traduzioni:
                if v in self.dizionario.dizionario[parts[0]]:
                    traduzioni.remove(v)
            self.dizionario.dizionario[parts[0]].extend(traduzioni)
            try:
                with open(self.filename, "r", encoding="utf-8") as file:
                    lines = file.readlines()
                with open(self.filename, "w", encoding="utf-8") as file:
                    for line in lines:
                        if parts[0] in line.strip().split(" "):
                            print("entrato")
                            line = f"{parts[0]} {" ".join(traduzioni)}\n"
                            file.write(line)
                        else: file.write(line)
                print(f"Parola '{parts[0]}' e traduzioni aggiunte al file.")
            except IOError:
                print(f"Errore: Problema nell'apertura o scrittura del file '{self.filename}'.")
        else:
            self.dizionario.dizionario[parts[0]] = traduzioni
            try:
                with open(self.filename, "a", encoding="utf-8") as file:
                    file.write(f"\n{parts[0]} {' '.join(traduzioni)}")
                print(f"Parola '{parts[0]}' e traduzioni aggiunte al file.")
            except IOError:
                print(f"Errore: Problema nell'apertura o scrittura del file '{self.filename}'.")
        print(f"Parola '{parts[0]}' aggiunta con traduzioni: {parts[1]}")

    def handleTranslate(self, query):
        # query is a string <parola_aliena>
        query = query.lower()
        try:
            traduzione = self.dizionario.dizionario[query]
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
        for word in self.dizionario.dizionario:
            if re.match(pattern, word):
                matched_words.append(word)
        if matched_words:
            print(f"Corrispondenze: {', '.join(matched_words)}")
            for w in matched_words:
                self.handleTranslate(w)
        else:
            print(f"Nessuna parola corrisponde alla query '{query}'.")





