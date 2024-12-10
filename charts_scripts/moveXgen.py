import pandas as pd
import matplotlib.pyplot as plt

# Leggi il file CSV
file_path = "data/csv/complete_moves.csv"  # Sostituisci con il percorso del tuo file
df = pd.read_csv(file_path)

nomi = ["Kanto", "Johto", "Hoenn", "Sinnoh", "Unima", "Kalos", "Alola", "Galar", "Paldea"]

gen_counts = df['Gen'].value_counts().reindex(range(1, len(nomi) + 1), fill_value=0)

plt.figure(figsize=(10, 6))
plt.barh(nomi, gen_counts.values, color='#6baed6', zorder=3)

plt.title("Numero di Mosse per Generazione nei Pokémon", fontsize=14)
plt.grid(axis='x', linestyle='--', alpha=0.7, zorder=0) 

plt.gca().invert_yaxis()

ax = plt.gca()
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(True)
ax.spines['bottom'].set_visible(True)

plt.tight_layout()
plt.show()
