class Quiz:
    def __init__(self):
        self.domande = [
            {"domanda": "qual e il tipo di dato per True/False in Python?", "opzioni": ["String", "Boolean", "Integer", "Float"], "risposta_corretta": 1},
            {"domanda": "Come si crea una lista vuota in Python?", "opzioni": ["list()", "[]", "new list", "Entrambi A e B"], "risposta_corretta": 3},
            {"domanda": "Quale parola chiave crea una funzione?", "opzioni": ["function", "def", "define", "func"], "risposta_corretta": 1},
            {"domanda": "cosa ritorna len([1,2,3])?", "opzioni": ["1", "2", "3", "Error"], "risposta_corretta": 2}
        ]
        self.punteggio = 0

    def avvia(self):
        print("\n"+"="*50)
        print("QuIz PyThOn")
        print("="*50+"\n")
        for i, domanda in enumerate(self.domande,1):
            print(f"Domanda {i}/{len(self.domande)}")
            print(f"❓❓{domanda['domanda']}\n")
            for j, opzione in enumerate(domanda['opzioni'],1):
                print(f" {j}.{opzione}")
            risposta = int(input("\nLa tua risposta (numero):"))  # Rimuovi try/except per semplicità o adatta
            if 1<=risposta<=len(domanda['opzioni']) and risposta - 1 == domanda['risposta_corretta']:
                print("CORRETTO\n")
                self.punteggio +=1
            else:
                print("❌📛Sbagliato")
                print(f" La risposta corretta era: {domanda['opzioni'][domanda['risposta_corretta']]}\n")
        self.mostra_risultato()

    def mostra_risultato(self):
        print("\n"+"="*50)
        print("RiSuLTaTo FiNaLe")
        print("="*50+"\n")
        percentuale = (self.punteggio/len(self.domande))*100
        print(f"Risposte corrette: {self.punteggio}/{len(self.domande)}")
        print(f"Percentuale: {percentuale:.1f}%\n")
        if percentuale >= 80:
            print("Eccellente conosci python")
        elif percentuale >= 60:
            print("Buono")
        else:
            print("continua a studiare")
        print()

quiz = Quiz()
quiz.avvia()
