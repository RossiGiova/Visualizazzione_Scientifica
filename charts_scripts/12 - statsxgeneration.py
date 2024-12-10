import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/csv/pokemon_complete.csv")
df = df[~df["form_type"].isin(["mega", "giga", "archeo", "form"])]


generations = ["Kanto", "Johto", "Hoenn", "Sinnoh", "Unima", "Kalos", "Alola", "Galar", "Paldea"]

stats_columns = ['hp', 'attack', 'defense', 'special-attack', 'special-defense', 'speed']

colors = [
    'lightgreen',  # Rosso tenue per HP
    'lightcoral',  # Arancione tenue per Attack
    'cornflowerblue',  # Giallo tenue per Defense
    'lightsalmon',  # Blu tenue per Special-Attack
    'lightblue',  # Verde tenue per Special-Defense
    'plum'   # Viola tenue per Speed
]


avg_stats_by_gen = []
for i in range(1, 10):
    generation_data = df[df['generation'] == i]
    avg_stats = generation_data[stats_columns].mean().values
    avg_stats_by_gen.append(avg_stats)

avg_stats_df = pd.DataFrame(avg_stats_by_gen, columns=stats_columns, index=generations)

avg_stats_df.plot(kind="bar", figsize=(14, 8), width=0.8, color=colors, zorder = 2)
plt.title("Media delle Statistiche per Generazione", fontsize=16)
plt.xticks(rotation=0)
plt.legend(title="Statistiche", bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.grid(axis='y', linestyle='--', alpha=0.7, zorder = 1)

ax = plt.gca()
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(True)
ax.spines['bottom'].set_visible(True)

plt.show()
