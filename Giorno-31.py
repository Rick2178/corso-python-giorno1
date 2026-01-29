# COPIA DAL PRIMO PRINT ALLA FINE - SOSTITUISCI TUTTO IL FILE

print("=" * 50)
print("Sistema Gestione Magazzino - PROFESSIONALE")
print("=" * 50)
print()


class Prodotto:
    """Sistema professionale gestione magazzino."""

    def __init__(self, nome, prezzo, quantita):
        self.nome = nome
        self.prezzo = prezzo
        self.quantita = quantita
        self.vendite = 0

    def vendi(self, quantita):
        if quantita <= self.quantita:
            self.quantita -= quantita
            self.vendite += quantita
            return f"✅ Venduti {quantita} x {self.nome}"
        else:
            return f"❌ Non abbastanza! Stock: {self.quantita}"

    def ricaricare(self, quantita):
        self.quantita += quantita
        return f"📦 Ricaricati {quantita} x {self.nome}"

    def mostra_info(self):
        print(f"\n{'='*50}")
        print(f"📱 PRODOTTO: {self.nome}")
        print(f"{'='*50}")
        print(f"💰 Prezzo: €{self.prezzo:.2f}")
        print(f"📦 Stock: {self.quantita}")
        print(f"📊 Vendite: {self.vendite}")
        print(f"💵 Ricavato: €{self.prezzo * self.vendite:.2f}")
        print(f"{'='*50}\n")

    def profitto_totale(self):  # ← QUESTO MANCAVA
        return self.prezzo * self.vendite


# TEST SISTEMA
print("🧪 SIMULAZIONE MAGAZZINO\n")

prodotti = [
    Prodotto("iPhone 15 Pro", 999, 50),
    Prodotto("Samsung S24", 899, 30),
    Prodotto("Pixel 8", 799, 40)
]

# VENDITE
for p in prodotti:
    print(p.vendi(3))

print("\n📊 REPORT MAGAZZINO:")
for p in prodotti:
    p.mostra_info()

# TOTALE
ricavato_totale = sum(p.profitto_totale() for p in prodotti)
print(f"\n💰 RICAVATO TOTALE: €{ricavato_totale:,.2f}")
print("🎉 SISTEMA MAGAZZINO OPERATIVO!")
