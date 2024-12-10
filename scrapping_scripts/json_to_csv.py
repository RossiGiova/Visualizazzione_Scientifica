import json, csv

def main():
    dati = []
    for i in range(1, 1026, 1):
        dato = []
        with open(f"pokemons/{i}.json") as file:
            json_file = json.load(file)
            #print(json_file["id"], json_file["name"])
            dato.append(json_file["id"])
            dato.append(json_file["name"])
            if len(json_file["types"]) == 1:
                types = [json_file["types"][0]["type"]["name"], "Null"]
            elif len(json_file["types"]) == 2:
                types = [json_file["types"][0]["type"]["name"], json_file["types"][1]["type"]["name"]]
            else:
                raise(f"Bro guarda qui {i}")
            dato = dato + types
            total_stat = 0
            for stat in json_file["stats"]:
                #print(stat["base_stat"], stat["stat"]["name"])
                dato.append(stat["base_stat"])
                total_stat += int(stat["base_stat"])
            #print("Total: ", total_stat)
            dato.append(total_stat)
            #print(types)
            #print(json_file.keys())
            dati.append(dato)
            
    with open(f"all_pokemon.csv", "w", newline="") as pokemon:
        lettore = csv.writer(pokemon, delimiter=",")
        lettore.writerow(["Pokedex", "name", "type_1", "type_2", "hp", "attack", "difense", "special-attack", "special-defense", "speed", "total"])
        lettore.writerows(dati)



main()