import pandas as pd
import matplotlib.pyplot as plt

file_path = "data/csv/complete_moves.csv"
df = pd.read_csv(file_path)

nomi = ["Kanto", "Johto", "Hoenn", "Sinnoh", "Unima", "Kalos", "Alola", "Galar", "Paldea"]

type_counts = df['Type'].value_counts()

plt.figure(figsize=(12, 6))
plt.barh(type_counts.index, type_counts.values, color='#6baed6', zorder=2)

plt.title("Numero di Mosse per Tipo di Pokémon", fontsize=14)

for i, v in enumerate(type_counts.values):
    plt.text(i, v + 1, str(v), ha='center', fontsize=10)

plt.grid(axis="x", zorder = 0)

ax = plt.gca()
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(True)
ax.spines['bottom'].set_visible(True)

plt.tight_layout()
plt.show()
