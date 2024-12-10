import os
import pandas as pd
import matplotlib.pyplot as plt

percorso = "data/csv/tournaments"

#print(len(os.listdir(percorso)))



all_comp_poke = {}

for file in os.listdir(percorso):
    df = pd.read_csv(f"{percorso}/{file}")
    for team in df["Team_Pokémon"]:
        for poke in team.split(","):
            #print(poke.strip())
            all_comp_poke[poke.strip()] = all_comp_poke.get(poke.strip(), 0) + 1

ordered_poke = dict(sorted(all_comp_poke.items(), key=lambda item: item[1]))

print(ordered_poke.keys())

pokemon_names = list(ordered_poke.keys())[254:]
usage_counts = list(ordered_poke.values())[254:]

#print(len(pokemon_names))

plt.figure(figsize=(10, 6))
plt.barh(pokemon_names, usage_counts, color='skyblue')
plt.title("Pokèmon più utilizzati nei tornei")
plt.grid(axis='x', linestyle='--', alpha=0.6)

ax = plt.gca()
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(True)
ax.spines['bottom'].set_visible(True)

plt.tight_layout()

# Mostrare il grafico
plt.show()