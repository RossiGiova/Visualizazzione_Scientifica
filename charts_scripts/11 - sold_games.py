import pandas as pd
import matplotlib.pyplot as plt


file_name = "data/csv/games_sold.csv"
df = pd.read_csv(file_name)

df = df.sort_values(by="Anno", ascending=True)

plt.figure(figsize=(10, 8))
plt.barh(df['Titolo'], df['Unità vendute'], color='skyblue', zorder=2)
plt.xlabel('Unità vendute (Milioni)')
plt.title('Vendite dei giochi Pokémon per anno di uscita')
plt.grid(axis="x", linestyle='--', zorder=1)
plt.gca().invert_yaxis()
plt.tight_layout()

plt.show()
