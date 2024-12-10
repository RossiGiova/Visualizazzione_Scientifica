import requests
import json

def download_json(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            
            return data
        else:
            print(f"Errore durante il download del JSON. Status code: {response.status_code}")
            return None
    except Exception as e:
        print(f"Si è verificato un errore: {e}")
        return None

def main():
    for i in range(1, 1026, 1):
        url = f"https://pokeapi.co/api/v2/pokemon/{i}"
        json_data = download_json(url)
        if json_data != None:
            formated_data = json.dumps(json_data, indent=4)
            with open(f"pokemons/{i}.json", "w") as file:
                file.write(formated_data)
main()