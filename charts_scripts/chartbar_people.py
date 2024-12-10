import os
import pandas as pd
import matplotlib.pyplot as plt

percorso = "data/csv/tournaments"

print(len(os.listdir(percorso)))

all_nationality = {}

for file in os.listdir(percorso):
    df = pd.read_csv(f"{percorso}/{file}")
    new_dict = df["Nazionalità"].value_counts().to_dict()
    for key, value in new_dict.items():
        all_nationality[key] = all_nationality.get(key, 0) + value


ordered_nationality = dict(sorted(all_nationality.items(), key=lambda item: item[1]))

print(ordered_nationality)

nationality_names = list(ordered_nationality.keys())
nationality_counts = list(ordered_nationality.values())

#print(len(pokemon_names))

plt.figure(figsize=(10, 6))
plt.barh(nationality_names, nationality_counts, color='skyblue')
plt.title("Pokèmon più utilizzati nei tornei")
plt.grid(axis='x', linestyle='--', alpha=0.6)

ax = plt.gca()
ax.spines['top'].set_visible(False) 
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(True)
ax.spines['bottom'].set_visible(True) 

plt.tight_layout()

plt.show()