

#esercizio contatore caffe
print("="*50)
print("CONATORE VENDTE Caffe")
print("="*50)

vendite = ["espresso", "cappuccino", "espresso", "cornetto", "cappuccino"]

# Conta ogni tipo
for caffe in vendite:
    print(f"Venduto: {caffe}")

print(f"\n📊 Report:")
print(f"Espresso: {vendite.count('espresso')}") 
print(f"Cappuccino: {vendite.count('cappuccino')}")
print(f"Cornetto: {vendite.count('cornetto')}")


print("="*50)
print("la lista della spesa")
print("="*50)

spesa=["pane","cornetti","coca cola","prsciutto","fazzoletti"]
for i, articolo in enumerate (spesa,1):
    print(f"{i}.{articolo}")

spesa.append("mele")
print(f"\n Totale articoli:{len(spesa)}")

spesa.remove("pane")
print("\n dopo aver tolto il pane")
for i, articolo in enumerate (spesa,1):
    print(f"{i}.{articolo}")

print()
