import requests
import json

def vind_langste_username():
    # Verzend een GET verzoek naar de JSONPlaceholder API
    response = requests.get("https://jsonplaceholder.typicode.com/users")
    
    # Zet de JSON response om naar een Python object
    data = json.loads(response.text)

    # Initieer de lengte variabele voor de langste gebruikersnaam en de bijbehorende gebruiker
    max_len = 0
    user_met_max_len = ''

    
    for user in data:
        username = user['username']  
        length = len(username)      
        
      
        if length > max_len:
            max_len = length          
            user_met_max_len = user['name']  

    return user_met_max_len, max_len

# Test de functie
naam, lengte = vind_langste_username()
print(f'De gebruiker met de langste gebruikersnaam is {naam} met een lengte van {lengte} karakters.') 