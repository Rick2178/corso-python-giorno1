#stampa
print("Benvenuto nella Programmazione di Pyton")
print("="*50)
#chiedi il nome
nome=input("Come ti chiami?")
#chiedi la citta
citta=input("da quale citta arrivi?")
#chiedi dove vivi
citta_dove_vivi=input("In quale citta vivi?")
# 3. Chiedi l'età
print(f"\nOk {nome}, dimmi di più...")
eta = input(" Quanti anni hai? ")
eta = int(eta)  # Converti in numero
# 4. Chiedi il lavoro attuale
lavoro = input("💼 Che lavoro fai oggi? ")

# 5. Calcola anni al nuovo lavoro
anni_al_lavoro = 90 - (eta % 10)  # Formula magica
print("\n" + "=" * 50)
print(f"Ciao {nome}")
print(f"Che bello arrivi dalla magica {citta}")

print(f"Hai {eta}")
print(f"Oggi  Riccardo {lavoro}....ma ancora per poco fidati!")
print()
print("🚀 TRA POCHI GIORNI SARAI:")
print(f"   👨‍💻 Python Developer a {citta_dove_vivi}")
print(f"   💰 Con uno stipendio nuovo")
print(f"   ⏰ In {anni_al_lavoro} giorni esatti!")
print("=" * 50)
# CHIEDI L'OBIETTIVO
obiettivo = input("\n🎯 Quale lavoro sogni? ")
print(f"\n💭 {nome}, {obiettivo} ti aspetta!")
print("   Python è la chiave. Continua! 💪")

print("=" * 50)

