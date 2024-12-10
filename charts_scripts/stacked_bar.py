import matplotlib.pyplot as plt
import numpy as np
import csv

def getPokemonStats():
    pokedex = int(input("Inserisci il numero di pokedex: "))
    with open('data/csv/pokemon_not_complete.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for index, values in enumerate(csv_reader):
            if index == pokedex:
                # 8 hp, 5 attack, 6 defense, 7 sp attack, 4 sp defense, 9 speed 
                print(index, values[1], values[8], values[5], values[6], values[7], values[4], values[9])
                return values[1], [int(values[8]), int(values[5]), int(values[6]), int(values[7]), int(values[4]), int(values[9])]

spoke_labels = ['special defense', 'attack', 'defense', 'special attack', 'hp', 'speed']

npok1, pokemon1 = getPokemonStats()
npok2, pokemon2 = getPokemonStats()

bar_width = 0.4
indices = np.arange(len(spoke_labels))

fig, ax = plt.subplots(figsize=(10, 6))

for i, label in enumerate(spoke_labels):
    if pokemon1[i] > pokemon2[i]:

        ax.bar(indices[i], pokemon1[i], bar_width, color='skyblue', label=npok1 if i == 0 else "")
        ax.bar(indices[i], pokemon2[i], bar_width, color='salmon', label=npok2 if i == 0 else "")
    else:

        ax.bar(indices[i], pokemon2[i], bar_width, color='salmon', label=npok2 if i == 0 else "")
        ax.bar(indices[i], pokemon1[i], bar_width, color='skyblue', label=npok1 if i == 0 else "")

ax.set_xlabel('Statistiche')
ax.set_xticks(indices)
ax.set_xticklabels(spoke_labels)
ax.legend()

plt.show()
