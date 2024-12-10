import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import CubicSpline

file_path = 'data/csv/pokemon_complete.csv'
pokedex_df = pd.read_csv(file_path)

pokedex_df = pokedex_df[~pokedex_df["form_type"].isin(["mega", "giga", "archeo", "form"])]
dati = pokedex_df["total"].to_list()

offset = 50
range_values = [f"{x}-{x+offset-1}" for x in range(150, 750, offset)]
range_counts = {ranges: 0 for ranges in range_values}

for dato in dati:
    for text in range_counts.keys():
        min_val, max_val = map(int, text.split("-"))
        if min_val < dato <= max_val:
            range_counts[text] += 1

x_labels = list(range_counts.keys())
y_values = list(range_counts.values())

x_numeric = np.arange(len(x_labels))

cs = CubicSpline(x_numeric, y_values)

x_dense = np.linspace(0, len(x_labels)-1, 500) 
y_dense = cs(x_dense)

plt.plot(x_dense, y_dense, color='b', label='Curva Interpolata')
plt.plot(x_numeric, y_values, 'bo', label='Dati Originali')

for i, value in enumerate(y_values):
    plt.text(x_numeric[i], value, str(value), ha='center', va='bottom')


plt.title("Distribuzione delle statistiche totali dei Pokémon (range 50)")

plt.xticks(x_numeric, x_labels, rotation=0)
plt.legend()


#plt.tight_layout()
plt.show()
