import pandas as pd
import matplotlib.pyplot as plt

file_name = "data/csv/only_competitive.csv"
df = pd.read_csv(file_name)

plt.figure(figsize=(10, 6))
plt.scatter(df['defense'], df['special-defense'], color='skyblue', alpha=0.7, edgecolor='k')
plt.title('Relazione tra Difesa e Difesa speciale dei Pokémon')
plt.xticks([x for x in range(0, 226, 25)])
plt.yticks([y for y in range(0, 226, 25)])
plt.xlabel('Difesa')
plt.ylabel('Difesa speciale')
plt.grid(alpha=0.5)

plt.tight_layout()
plt.show()
