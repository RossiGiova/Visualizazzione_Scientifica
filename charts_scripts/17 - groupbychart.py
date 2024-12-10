import csv
import pandas as pd
import matplotlib.pyplot as plt


def getPokemonStats():
    pokedex = input("Inserisci il numero di Pokedex: ")
    with open('data/csv/only_competitive.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for _, values in enumerate(csv_reader):
            if values[0] == pokedex:
                print(values)
                # Indici: 8 = HP, 5 = Attack, 6 = Defense, 7 = Sp. Attack, 4 = Sp. Defense, 9 = Speed
                return values[1], [int(values[5]), int(values[6]), int(values[7]), int(values[8]), int(values[9]), int(values[10])]
            

def getAverageStats():
    df = pd.read_csv('data/csv/only_competitive.csv')
    avg_stats = [
        df['hp'].mean(),
        df['attack'].mean(),
        df['defense'].mean(),
        df['special-attack'].mean(),
        df['special-defense'].mean(),
        df['speed'].mean()
    ]
    return avg_stats

def plotComparison():

    pokemon_name, pokemon_stats = getPokemonStats()

    avg_stats = getAverageStats()

    labels = ["hp", "attack", "defense", "special attack", "special defense", "speed"]

    x = range(len(labels))
    bar_width = 0.4 

    plt.figure(figsize=(10, 6))

    plt.bar([pos - bar_width / 2 for pos in x], pokemon_stats, width=bar_width, color='skyblue', label=pokemon_name, zorder=2)
    plt.bar([pos + bar_width / 2 for pos in x], avg_stats, width=bar_width, color='lightsalmon', label='Media Pokémon', zorder=2)

    plt.xticks(x, labels, fontsize=12)
    plt.grid(axis="y", linestyle="--", zorder=1)
    plt.title(f"Confronto tra {pokemon_name} e la Media Pokémon", fontsize=16)
    plt.legend()
    plt.tight_layout()

    ax = plt.gca()
    ax.spines['top'].set_visible(False) 
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(True) 
    ax.spines['bottom'].set_visible(True)  

    plt.show()

plotComparison()
