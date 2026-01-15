

import json
from typing import List, Dict

class Biblioteca:
    def __init__(self):  # Corretto: __init__ con doppia underscore
        self.libri = []
        self.carica_da_file()  # Chiamata corretta

    def aggiungi_libro(self, titolo, autore, letto=False):
        libro = {
            "titolo": titolo,
            "autore": autore,
            "letto": letto
        }
        self.libri.append(libro)  # Corretto: append, non appened
        print(f"'{titolo}' aggiunto!")

    def mostra_libri(self):
        print("\n" + "="*60)
        print(" La Mia Biblioteca")
        print("="*60 + "\n")
        for i, libro in enumerate(self.libri, 1):
            stato = "LETTO" if libro["letto"] else "DA LEGGERE"
            print(f"{i}. {libro['titolo']}")
            print(f"   Autore: {libro['autore']}")
            print(f"   Status: {stato}\n")

    def cerca_libro(self, titolo):
        for libro in self.libri:  # Ritorna il libro trovato
            if titolo.lower() in libro["titolo"].lower():
                return libro  # Corretto: return libro, non None
        return None

    def marca_come_letto(self, titolo):
        libro = self.cerca_libro(titolo)
        if libro:
            libro["letto"] = True
            print(f"✓ '{titolo}' segnato come letto!")
        else:
            print(f"❌ Libro '{titolo}' non trovato")

    def salva_su_file(self):
        with open("biblioteca.json", "w", encoding="utf-8") as f:
            json.dump(self.libri, f, indent=2, ensure_ascii=False)
        print("Biblioteca salvata su biblioteca.json")

    def carica_da_file(self):  # Indentazione corretta (metodo classe)
        try:
            with open("biblioteca.json", "r", encoding="utf-8") as f:
                self.libri = json.load(f)
            print("Dati caricati da file!")
        except FileNotFoundError:
            self.libri = []
            print("Nuova biblioteca creata (file non trovato)")

# Uso
mia_biblioteca = Biblioteca()
mia_biblioteca.aggiungi_libro("Clean Code", "Robert C. Martin")
mia_biblioteca.aggiungi_libro("The Pragmatic Programmer", "David Thomas")
mia_biblioteca.aggiungi_libro("Python Crash Course", "Eric Matthes", letto=True)

mia_biblioteca.mostra_libri()

mia_biblioteca.marca_come_letto("Clean Code")

mia_biblioteca.salva_su_file()

print("Programma completato!")
