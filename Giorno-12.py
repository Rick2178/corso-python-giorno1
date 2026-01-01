print("="*50)
print("Salva i tuoi appunti")
print("="*50)

#apri i file per scrivere
file=open("mio_progresso.txt","w")

#scrivi i tuoi dati
file.write("Giorno 12: il mio progresso Python\n")
file.write("="*50 + "\n\n")
file.write("cosa ho imparato:\n")
file.write("VARIABILI\n")
file.write("NUMERI E CALCOLI\n")
file.write("INPUT/OUTPUT\n")
file.write("IF/ELSE\n")
file.write("CICLI\n")
file.write("LISTE\n")
file.write("DIZIONARI\n")
file.write("FUNZIONI\n")
file.write("\n")
file.write("PROGETTI COMPLETATI:11\n")
file.write("GIORNI RIMANRNTI:79\n")

#chiudi il file
file.close()

print("File salvato: mio_progresso.txt\n")

#leggi file
file=open("mio_progresso.txt","r")
contenuto=file.read()
file.close()

print(" CONTENUTO DEL FILE : ")
print("="*50)
print(contenuto)
print("="*50)

