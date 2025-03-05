import translator
class Dictionary:
    def __init__(self, filename=None):
        self.filename = filename
        self.words = {}

    def addWord(self, word, translations):
        nuovetraduzioni = translations.strip().split(" ")
        if word in self.words:
            for v in nuovetraduzioni:
                if v in self.words[word]:
                    nuovetraduzioni.remove(v)
                    print(f"rimosso {v}")
            self.words[word].extend(nuovetraduzioni)
        else:
            self.words[word] = translations.strip().split(" ")
        print(f"Parola '{word}' aggiunta con traduzioni: {translations}")
        try:
            with open(self.filename, "a", encoding="utf-8") as file:
                file.write(f"\n{word} {' '.join(nuovetraduzioni)}")
            print(f"Parola '{word}' e traduzioni aggiunte al file.")
        except IOError:
            print(f"Errore: Problema nell'apertura o scrittura del file '{self.filename}'.")
    '''
    def translate(self, word):
        translator.Translator.handleTranslate(word)

    def translateWordWildCard(self, query):
        translator.Translator.handleWildCard(query)
    '''