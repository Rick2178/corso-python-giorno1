print("="*50)
print("Profilo personale"+"📋")
print("="*50)

profilo={"nome":"Riccardo",
         "eta" : 47,
         "citta":"Roma",
         "lavoro attuale":"Imprenditore",
         "lavoro futuro": "Programmatore",
         "linguaggio": "python ed altri",
         "obbiettivo":"nuovo lavoro entro 90gg"
         }

#stampa
print(f"\n Ciao,{profilo["nome"]}!")
print(f"hai {profilo["eta"]}")
print(f"so che abiti a {profilo["citta"]}")
print(f"attualmente sei un {profilo["lavoro attuale"]}")
print(f"stai praticano per diventare un {profilo["lavoro futuro"]}")
print(f"stai provando ad imparare il linguaggio {profilo["linguaggio"]}")
print(f"obbiettivo :{profilo["obbiettivo"]}")

profilo["giorni di studio"]=9
profilo["progetti completati"]=5

print(f"\n Progresso :")
print(f" Giorni di studio completati:{profilo["giorni di studio"]}")
print(f"progetti completati : {profilo["progetti completati"]}")

print()
