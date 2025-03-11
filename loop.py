# 10/10/2024
# Kyran Koehler

print("Getallen van 1 t/m 10:")
for i in range(1, 11):
    print(i)

print()

print("Even getallen van 12 t/m 36:")
for i in range(12, 37, 2):
    print(i)


leeftijd = int(input("Voer je leeftijd in: "))
if leeftijd >= 18:
    print(f"Je bent 18, zorg ervoor dat je een zorgverzekering heb afgesloten")

else: 
    print("Je hoeft nog geen zorgverzekering af te sluiten")