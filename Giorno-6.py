print("="*50)
print("📊Termometro Intelligente")
print("="*50)

print("misura la tua temperatura, di quanto é?\n")

temperatura = float(input("Quale é la tua temperatura (°C)?"))

print("\n+" + "="*50)
print("DIAGNOSI")  

#decisioni intelligenti

if temperatura < 36.5 :
    print("🛌BASSA!! Riposa e resta al caldo")
elif temperatura <= 37.5 :
    print("🔅NORMALE!! ti senti bene")
elif temperatura <=38.5 :
    print("😫FEBBRE!!prendi un aspirina e mettiti a riposo ")
else :
    print("💊FEBBRE ALTA!! Meglio chiamare un medico")

print("="*50)
                                                    