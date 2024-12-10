import pandas as pd
import matplotlib.pyplot as plt

file_name = "data/csv/only_competitive.csv"
df = pd.read_csv(file_name)

type_counts = pd.concat([df['type_1'], df['type_2']]).value_counts().to_dict()
type_counts.pop("Null")

plt.figure(figsize=(12, 6))
plt.bar(type_counts.keys(), type_counts.values(), color='skyblue', zorder=2)
plt.title('Conteggio Totale dei Pokémon per Tipo (Type 1 + Type 2)')
plt.grid(axis='y', linestyle='--', alpha=0.7, zorder = 1)

plt.tight_layout()
plt.show()
