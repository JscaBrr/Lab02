import re
class Translator:

    def __init__(self, classedizionario): #class(class)
      self.classedizionario = classedizionario

    def printMenu(self):
     print("\nMenu:")
     print("1. Aggiungi una nuova parola")
     print("2. Cerca una traduzione")
     print("3. Cerca con wildcard")
     print("4. Esci")

    def handleAdd(self, entry):
        if not re.fullmatch(r"[A-Za-zÀ-ÖØ-öø-ÿ\s]+", entry):
            print("Errore: la stringa contiene caratteri non validi.")
            return
        entry = entry.lower()
        parts = entry.split(" ",1)
        traduzioni = parts[1].split(" ")
        if parts[0] in self.classedizionario.dizionario:
            for t in traduzioni:
                if t in self.classedizionario.dizionario[parts[0]]:
                    traduzioni.remove(t)
            self.classedizionario.dizionario[parts[0]].extend(traduzioni)
        else:
                self.classedizionario.dizionario[parts[0]] = traduzioni
        try:
            with open(self.classedizionario.filename, "w", encoding="utf-8") as file:
                for i in self.classedizionario.dizionario:
                    if len(self.classedizionario.dizionario[i]) == 1:
                        file.write(f"{i} {self.classedizionario.dizionario[i][0]}\n")
                    else:
                        file.write(f"{i} {" ".join(self.classedizionario.dizionario[i])}\n")
            print("Esecuzione andata a buon fine - traduzione aggiunta al dizionario")
        except FileNotFoundError:
            print("ERRORE: File non trovato")
            return

    def handleTranslate(self, query):
       if query.lower() in self.classedizionario.dizionario:
           print(f"Traduzione di {query}: {" ".join(self.classedizionario.dizionario[query.lower()])}")
       else:
           print("ERRORE: Parola non trovata!")

    def handleWildCard(self,query):
        pattern = query.lower().replace("?", ".")
        for i in self.classedizionario.dizionario:
            if re.fullmatch(pattern, i):
                print(f"Traduzione di {query}: {" ".join(self.classedizionario.dizionario[i.lower()])}")
                return
        print("ERRORE: Parola non trovata!")


