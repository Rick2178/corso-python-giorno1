print("="*50)
print("📊Termometro Intelligente")
print("="*50)


print("misura la tua temperatura , di quanto é?\n")

nome = input("Come ti chiami ?")
temperatura = float(input(f"{nome}, qual è la tua temperatura? "))

print("\n+" + "="*50)
print("DIAGNOSI")  

#decisioni intelligenti

if temperatura < 36.5 :
    print(f"{nome}🛌Temperatura BASSA!! Riposa e resta al caldo")
elif temperatura <= 37.5 :
    print(f"{nome}🔅Temperatura NORMALE!! ti senti bene")
elif temperatura <=38.5 :
    print(f"{nome}😫mi dispiace hai la FEBBRE!!prendi un aspirina e mettiti a riposo ")
else :
    print(f"{nome}💊purtroppo hai la FEBBRE MOLTO ALTA!! Meglio chiamare un medico")

print("="*50)
                                                    