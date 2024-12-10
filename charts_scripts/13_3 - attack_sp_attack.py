import pandas as pd
import matplotlib.pyplot as plt

file_name = "data/csv/only_competitive.csv"
df = pd.read_csv(file_name)

plt.figure(figsize=(10, 6))
plt.scatter(df['attack'], df['special-attack'], color='lime', alpha=0.6, edgecolor='k')
plt.title('Relazione tra Attacco e Attacco speciale dei Pokémon')
plt.xticks([x for x in range(0, 226, 25)])
plt.yticks([y for y in range(0, 226, 25)])
plt.xlabel('Attacco')
plt.ylabel('Attacco speciale')
plt.grid(alpha=0.5)

plt.tight_layout()
plt.show()
