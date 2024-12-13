# Eingabe der beiden Zahlen
zahl1 = float(input("Bitte gib die erste Zahl ein: "))
zahl2 = float(input("Bitte gib die zweite Zahl ein: "))

# Berechnungen
summe = zahl1 + zahl2
differenz = zahl1 - zahl2
multiplikation = zahl1 * zahl2

# Verhindern einer Division durch Null
if zahl2 != 0:
    division = zahl1 / zahl2
else:
    division = "Nicht definiert (Division durch Null)"

# Ausgabe der Ergebnisse
print(f"Summe: {summe}")
print(f"Differenz: {differenz}")
print(f"Multiplikation: {multiplikation}")
print(f"Division: {division}")
