def caricadizionario(filename):
    dizionario = {}
    try:
        with open(filename, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip().split(" ",1)
                if len(line[1].split(" ")) > 1:
                    dizionario[line[0]] = [line[1].split(" ")]
                else : dizionario[line[0]] = [line[1]]
    except FileNotFoundError:
        print("ERRORE: File non trovato")
    return dizionario

class Dictionary:
    def __init__(self, filename):
        self.filename = filename
        self.dizionario = caricadizionario(filename)

    def __str__(self):
        return self.dizionario


