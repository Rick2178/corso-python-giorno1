print("="*60)
print("Programma sistema di gestione voti")
print("="*60)

# dizionario per voti
voti = {}

# funzione per aggiungere un voto
def aggiungi_voto(nome_studente, voto):
    if nome_studente not in voti:
        voti[nome_studente] = []
    voti[nome_studente].append(voto)
    print(f"Voto {voto} aggiunto a {nome_studente}")

# funzione per calcolare la media
def calcola_media(nome_studente):
    if nome_studente in voti and len(voti[nome_studente]) > 0:
        lista_voti = voti[nome_studente]
        media = sum(lista_voti) / len(lista_voti)
        return media
    return None

# funzione per salvare su file
def salva_su_file():
    with open("voti_studenti.txt", "w", encoding="utf-8") as file:
        file.write("REGISTRO VOTI\n")
        file.write("="*60 + "\n\n")

        for studente, voti_lista in voti.items():
            media = calcola_media(studente)
            file.write(f"Studente: {studente}\n")
            file.write(f"Voti: {voti_lista}\n")
            file.write(f"Media: {media:.2f}\n")

            if media is not None and media >= 7:
                file.write("Status: ✅ PROMOSSO\n")
            else:
                file.write("Status: ⚠ INSUFFICIENTE\n")

            file.write("-"*60 + "\n")

    print("\nDati salvati su voti_studenti.txt")

# aggiungi alcuni voti
print("\nAggiungo voti...\n")
aggiungi_voto("Riccardo", 8)
aggiungi_voto("Riccardo", 7.5)
aggiungi_voto("Riccardo", 7)
aggiungi_voto("Riccardo", 8.5)

print("\nAggiungo voti...\n")
aggiungi_voto("Marco", 6)
aggiungi_voto("Marco", 7.5)
aggiungi_voto("Marco", 7)
aggiungi_voto("Marco", 5.4)

print("\nAggiungo voti...\n")
aggiungi_voto("Laura", 5)
aggiungi_voto("Laura", 5)
aggiungi_voto("Laura", 7)

# mostra il riepilogo
print("\n" + "="*60)
print("Riepilogo Voti")
print("="*60 + "\n")

for studente in voti.keys():
    media = calcola_media(studente)
    print(f"👨‍🎓 {studente}: media {media:.2f}")
    if media >= 7:
        print("Status: ✅ PROMOSSO\n")
    else:
        print("Status: ⚠ INSUFFICIENTE\n")

# salva su file
salva_su_file()

# leggi da file
print("\nLEGGO DA FILE:")
print("="*60)
with open("voti_studenti.txt", "r", encoding="utf-8") as file:
    print(file.read())
