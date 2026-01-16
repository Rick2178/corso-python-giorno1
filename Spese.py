class GestioneSpeseMensili:
    def __init__(self):
        self.spese = {}

    def aggiungi_spesa(self, categoria, descrizione, importo):
        if categoria not in self.spese:
            self.spese[categoria] = []
        self.spese[categoria].append({"descrizione": descrizione, "importo": importo})
        print(f"✅ Spesa aggiunta: {descrizione} (Euro {importo:.2f})")

    def mostra_spese(self):
        print("\n" + "="*60)
        print("💰 GESTIONE SPESE MENSILI - REPORT COMPLETO")
        print("="*60 + "\n")

        totale_mese = 0

        for categoria, lista_spese in self.spese.items():
            print(f"📂 {categoria.upper()}")
            print("-" * 40)
            subtotale = 0

            for spesa in lista_spese:
                print(f"   • {spesa['descrizione']}: € {spesa['importo']:.2f}")
                subtotale += spesa['importo']

            print(f"   🧮 SUBTOTALE {categoria.upper()}: € {subtotale:.2f}")
            print("-" * 40)
            totale_mese += subtotale

        print("="*60)
        print(f"💎 TOTALE MESE: € {totale_mese:.2f}")
        print("="*60 + "\n")

    def categoria_piu_cara(self):
        if not self.spese:
            return None, 0
        
        max_categoria = None
        max_importo = 0

        for categoria, lista_spese in self.spese.items():
            subtotale = sum(s['importo'] for s in lista_spese)
            if subtotale > max_importo:
                max_importo = subtotale
                max_categoria = categoria

        return max_categoria, max_importo

# 🚀 PROGRAMMA PRINCIPALE - COPIA E INCOLLA
if __name__ == "__main__":
    # Crea gestore
    gestore = GestioneSpeseMensili()

    # Aggiungi spese reali (per il tuo caffè a Budapest!)
    gestore.aggiungi_spesa("cibo", "Spesa supermercato", 65.00)
    gestore.aggiungi_spesa("cibo", "Ristorante clienti", 35.00)
    gestore.aggiungi_spesa("trasporti", "Benzina auto", 50.00)
    gestore.aggiungi_spesa("trasporti", "Manutenzione auto", 80.00)
    gestore.aggiungi_spesa("intrattenimento", "Cinema relax", 15.00)
    gestore.aggiungi_spesa("intrattenimento", "Libri gestione", 25.00)

    # Mostra report completo
    gestore.mostra_spese()

    # Trova categoria più cara
    categoria_max, importo_max = gestore.categoria_piu_cara()
    if categoria_max:
        print(f"🔥 CATEGORIA PIÙ CARA: {categoria_max.upper()} (€ {importo_max:.2f})")
    else:
        print("Nessuna spesa registrata!")

    print("\n✨ PROGRAMMA COMPLETATO CON SUCCESSO!")
