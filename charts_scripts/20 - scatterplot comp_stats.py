import os
import pandas as pd
import matplotlib.pyplot as plt

data_path = "data/csv/tournaments"
competitive_file = "data/csv/only_competitive.csv"

df_competitive = pd.read_csv(competitive_file)

usage_frequency = {}

for file in os.listdir(data_path):
    if file.endswith('.csv'):
        df_tournament = pd.read_csv(f"{data_path}/{file}")

        pokemons = df_tournament['Team_Pokémon'].str.split(', ').explode()


        for name in pokemons:
            name = name.strip()
            usage_frequency[name] = usage_frequency.get(name, 0) + 1

df_usage = pd.DataFrame(list(usage_frequency.items()), columns=["comp_name", "Frequenza_Uso"])

merged_df = pd.merge(df_competitive, df_usage, on="comp_name", how="inner")

plt.figure(figsize=(10, 6))
plt.scatter(merged_df["total"], merged_df["Frequenza_Uso"], alpha=0.7, c='blue', edgecolors='w', s=80)
plt.title("Confronto tra Somma delle Statistiche Totali e Frequenza d'Uso nei Tornei")
plt.xlabel("Somma delle Statistiche Totali")
plt.ylabel("Occorrenze", rotation=0, labelpad=50)
plt.grid(True, linestyle='--', alpha=0.6)
print(merged_df[merged_df["total"] < 500].sort_values(by="Frequenza_Uso", ascending=True))
plt.tight_layout()
plt.show()