import json

# JSON data
json_data = """
{
    "mensen": [
        {"naam": "Johan Vermeulen", "leeftijd": 23},
        {"naam": "Ahmed Al-Hassan", "leeftijd": 26},
        {"naam": "María Rodríguez", "leeftijd": 30},
        {"naam": "Emma de Vries", "leeftijd": 28},
        {"naam": "Mohammed Abdulrahman", "leeftijd": 35}
    ]
}
"""

def vind_oudste_persoon(json_data):
    # Zet de JSON data om naar een Python object
    data = json.loads(json_data)

    # Initieer de variabelen voor maximale leeftijd en naam
    max_leeftijd = 0
    oudste_persoon = ""

    # Loop door de lijst van mensen
    for persoon in data["mensen"]:
        # Vergelijk de leeftijd met de huidige maximale leeftijd
        if persoon["leeftijd"] > max_leeftijd:
            max_leeftijd = persoon["leeftijd"]  # Update de maximale leeftijd
            oudste_persoon = persoon["naam"]     # Update de naam van de oudste persoon

    return oudste_persoon, max_leeftijd

# Test de functie
naam, leeftijd = vind_oudste_persoon(json_data)
print(f'De oudste persoon is {naam} met de leeftijd van {leeftijd} jaar.')