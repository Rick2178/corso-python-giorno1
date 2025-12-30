def somma_numeri(a,b):
    risultato=a+b
    return risultato

totale=somma_numeri(5,3)
print(totale)

print("="*50)
print("Le mie funzioni")
print("="*50)

#funzione saluta
def saluta(nome):
    print(f"Ciao , {nome}")
    print("benvenuto nel mio programma")
    print()

#funzione 2:calcola lo sconto
def applica_sconto(prezzo, percentuale_sconto):
    sconto=prezzo*(percentuale_sconto/100)
    prezzo_finale=prezzo-sconto
    return prezzo_finale

#funzione 3:verifica se un numero e pari
def e_pari(numero):
    if numero %2==0:
        return True
    else:
        return False
    
#uso le funzioni
saluta ("Riccardo")

prezzo_originale=100
sconto=20
prezzo_scontato=applica_sconto(prezzo_originale,sconto)
print(f"Prezzo originale: Euro{prezzo_originale}")
print(f"Sconto:{sconto}%")
print(f"Prezzo finale: Euro{prezzo_scontato:2f}\n")

#verifica numeri
for n in [3,4,5,6,7,8,9,10]:
    if e_pari(n):
        print(f"{n} é un numero pari")
    else:
        print(f"{n} é un numero dispari")

print()
