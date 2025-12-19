numero_persone=5
prezzo_per_persona=22.5
percentuale_mancia=15 # %

conto_prima_mancia=numero_persone*prezzo_per_persona
mancia=conto_prima_mancia*(percentuale_mancia/100)
conto_totale=conto_prima_mancia+mancia

print(f"Conto(senza mancia): Euro{conto_prima_mancia:.2f}")
print(f"Mancia({percentuale_mancia}%):Euro{mancia:.2f}")
print(f"TOTALE : Euro{conto_totale:.2f}")
print(f"A testa:Euro{conto_totale/numero_persone:.2f}")
