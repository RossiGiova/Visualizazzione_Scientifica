import csv

import csv

with open('all_pokemon.csv', 'r', newline='') as csvfile:
    reader = list(csv.reader(csvfile))
    reader[0].append("generation")
    for i in range(1,len(reader)):
        if 0 < i < 152:
            reader[i].append("1")
        
        elif 151 < i < 252:
            reader[i].append("2")

        elif 251 < i < 387:
            reader[i].append("3")
        
        elif 386 < i < 494:
            reader[i].append("4")
        
        elif 493 < i < 650:
            reader[i].append("5")

        elif 649 < i < 722:
            reader[i].append("6")
        
        elif 721 < i < 810:
            reader[i].append("7")
        
        elif 809 < i < 906:
            reader[i].append("8")
        
        else:
            reader[i].append("9")

with open(f"all_pokemons.csv", "w", newline="") as pokemon:
    lettore = csv.writer(pokemon, delimiter=",")
    lettore.writerows(reader)