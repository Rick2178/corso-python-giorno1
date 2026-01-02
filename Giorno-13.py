print("="*50)
print("Protezione dagli errori")
print("="*50)

# Funzione protettiva
def dividi_numeri():
    try:
        numero1 = float(input("\nInserisci il primo numero: "))
        numero2 = float(input("Inserisci il secondo numero: "))

        if numero2 == 0:
            print("❌ Non puoi dividere per 0")
        else:
            risultato = numero1 / numero2
            print(f"{numero1}/{numero2} = {risultato:.2f}")

    except ValueError:
        print("❌ Errore! Devi inserire numeri validi")
    except Exception as e:
        print(f"❌ Errore sconosciuto: {e}")

# Chiedi più volte
vuoi_continuare = True
while vuoi_continuare:
    dividi_numeri()
    risposta = input("\nVuoi provare ancora? (si/no): ")
    vuoi_continuare = risposta.lower() == "si"

print("\nArrivederci alla prossima!")
