import pandas as pd

competitive_pokemon_file = "data/csv/recent_comp.csv"
pokemon_stats_file = "data/csv/pokemon_complete.csv"

competitive_df = pd.read_csv(competitive_pokemon_file)
stats_df = pd.read_csv(pokemon_stats_file)

merged_df = pd.merge(competitive_df, stats_df, on="pokedex", how="inner")
merged_df = merged_df.sort_values(by="pokedex", ascending=True)
merged_df = merged_df.drop(columns=["name"])

merged_df.to_csv("data/csv/only_competitive.csv", index=False)

print(merged_df.head())
