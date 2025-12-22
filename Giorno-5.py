   
print("🌡 CONVERTITORE DI TEMPERATURE")
print("=" * 50)
print("°C Celsius ➡ Fahrenheit")
print("°F Fahrenheit ➡ Celsius")
print("=" * 50)

scelta = input("Scegli il tipo di conversione (°C o °F): ")

if scelta == "°C":
    celsius = float(input("Inserisci temperatura in °C: "))
    fahrenheit = (celsius * 9 / 5) + 32
    print(f"\n{celsius}°C = {fahrenheit:.1f}°F")

    if celsius <= 0:
        print("❄️ GHIACCIO! Tempo da sciarpa.")
    elif celsius <= 20:
        print("🥶 FREDDO. Metti il maglione.")
    elif celsius <= 30:
        print("🌤️ TEMPERATURA IDEALE!")
    else:
        print("🔥 CALDO! Aria condizionata!")

elif scelta == "°F":
    fahrenheit = float(input("Inserisci temperatura in °F: "))
    celsius = (fahrenheit - 32) * 5 / 9
    print(f"\n{fahrenheit}°F = {celsius:.1f}°C")

    if celsius <= 0:
        print("❄️ GHIACCIO! Tempo da sciarpa.")
    elif celsius <= 20:
        print("🥶 FREDDO. Metti il maglione.")
    elif celsius <= 30:
        print("🌤️ TEMPERATURA IDEALE!")
    else:
        print("🔥 CALDO! Aria condizionata!")

else:
    print("❌ Scelta non valida. Riavvia il programma.")
