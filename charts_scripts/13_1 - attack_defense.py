import pandas as pd
import matplotlib.pyplot as plt

file_name = "data/csv/only_competitive.csv"
df = pd.read_csv(file_name)

plt.figure(figsize=(10, 6))
plt.scatter(df['attack'], df['defense'], color='violet', alpha=0.9, edgecolor='k')
plt.title('Relazione tra Attacco e Difesa dei Pokémon')
plt.xticks([x for x in range(0, 226, 25)])
plt.yticks([y for y in range(0, 226, 25)])
plt.xlabel('Attacco')
plt.ylabel('Difesa')
plt.grid(alpha=0.5)

plt.tight_layout()
plt.show()
