import os
import pandas as pd
import matplotlib.pyplot as plt

percorso = "data/csv/tournaments"

print(f"Numero di file trovati: {len(os.listdir(percorso))}")

pokemon_trend = {}
pokemon_trend["numero giocatori"] = {}

for file in os.listdir(percorso):
    if file.endswith(".csv"):

        df = pd.read_csv(f"{percorso}/{file}")

        tournament_name = file.replace(".csv", "")
        
        pokemon_list = df['Team_Pokémon'].str.split(', ').explode()
        
        pokemon_counts = pokemon_list.value_counts()

        for pokemon, count in pokemon_counts.items():
            if pokemon not in pokemon_trend:
                pokemon_trend[pokemon] = {}
            pokemon_trend[pokemon][tournament_name] = count
        pokemon_trend["numero giocatori"][tournament_name] = len(df)

trend_df = pd.DataFrame(pokemon_trend).fillna(0).sort_index()

total_counts = trend_df.sum(axis=0).sort_values(ascending=False)

top_5_pokemon = total_counts.head(6).index
trend_df_top_5 = trend_df[top_5_pokemon]

trend_df_top_5_sampled = trend_df_top_5.iloc[::3]

plt.figure(figsize=(15, 8))
for i,pokemon in enumerate(trend_df_top_5_sampled.columns):
    if i == 0:
        plt.plot(trend_df_top_5_sampled.index, trend_df_top_5_sampled[pokemon], label=pokemon, linestyle="--", color="black")
    else:
        plt.plot(trend_df_top_5_sampled.index, trend_df_top_5_sampled[pokemon], label=pokemon)

plt.title("Trend dei 5 Pokémon più utilizzati nei Tornei (ogni 3 valori)", fontsize=16)
plt.xlabel("Torneo", fontsize=14)
plt.ylabel("Occorrenze", fontsize=14)
plt.grid(axis="y", linestyle="--")
plt.legend(title="Legenda", bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()

plt.show()
