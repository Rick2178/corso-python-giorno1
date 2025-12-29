print("=$="*50)
print("Calcolatore Budget Personale")
print("=$="*50)

budget= {
    "entrate":[
        (" stipendio " , 1350) ,
          (" lavori extra " , 300)
          ],
    "spese":[
        ("affitto",500),
        ("cibo",400),
        ("trasporti",100),
        ("intrattenimento",150),
        ("risparmi",500)]
}

#calcola entete
print("\n ENTRATE: ")
totale_entrate=0
for descrizione,importo in budget ["entrate"]:
    print(f" {descrizione} : Euro{importo}")
    totale_entrate=totale_entrate+importo

print(f"TOTALE ENTRATE : euro {totale_entrate}")

#calcola spese
print("\n SPESE")
totale_spese=0
for descrizione,importo in budget["spese"]:
    print(f" {descrizione}:Euro{importo}")
    totale_spese=totale_spese+importo
    print(f"TOTALE SPESE : euro {totale_spese}")

#il bilacio
bilancio=totale_entrate-totale_spese

print("n\=$="*50)
if bilancio > 0 :
    print(f"AVANZO : euro{bilancio}")
    print(" stai risparmiando!!!!")
elif bilancio == 0:
    print(" PAREGGIO : il budget e in equilibrio ma non stai risparmiando!!!!")
else:
    print(f" DEFICIT : euro {abs(bilancio)}")
    print(" Spendi troppo !!!!piu di quanto guadagni")

print("=$="*50)
print()
print()