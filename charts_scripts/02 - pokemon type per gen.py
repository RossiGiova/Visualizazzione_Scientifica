import pandas as pd
import matplotlib.pyplot as plt

file_path = 'data/csv/pokemon_complete.csv'
pokedex_df = pd.read_csv(file_path)

pokedex_df = pokedex_df[~pokedex_df["form_type"].isin(["mega", "giga", "archeo", "form"])]

type_colors = {
    "normal": "#A8A878", "fire": "#F08030", "water": "#6890F0", "electric": "#F8D030",
    "grass": "#78C850", "ice": "#98D8D8", "fighting": "#C03028", "poison": "#A040A0",
    "ground": "#E0C068", "flying": "#A890F0", "psychic": "#F85888", "bug": "#A8B820",
    "rock": "#B8A038", "ghost": "#705898", "dragon": "#7038F8", "dark": "#705848",
    "steel": "#B8B8D0", "fairy": "#F0B6BC"
}

regioni = {
    1: "Kanto",
    2: "Johto",
    3: "Hoenn",
    4: "Sinnoh",
    5: "Unima",
    6: "Kalos",
    7: "Alola",
    8: "Galar",
    9: "Paldea"
}
pokedex_df['region'] = pokedex_df['generation'].map(regioni)

type_counts = (
    pd.concat([pokedex_df[['region', 'type_1']].rename(columns={'type_1': 'type'}),
               pokedex_df[['region', 'type_2']].rename(columns={'type_2': 'type'})])
    .dropna(subset=['type'])
    .groupby(['region', 'type'])
    .size()
    .reset_index(name='count')
)

type_counts = type_counts[type_counts['type'] != 'Null']

type_order = type_counts.groupby('type')['count'].sum().sort_values(ascending=False).index

fig, axes = plt.subplots(nrows=3, ncols=3, figsize=(18, 12), constrained_layout=True)

max_count = type_counts['count'].max()

xticks = [i for i in range(0, max_count + 1, 5)]

for idx, (ax, region) in enumerate(zip(axes.flat, regioni.values())):
    region_data = type_counts[type_counts['region'] == region]
    colors = region_data['type'].map(type_colors)
    ax.barh(
        region_data['type'],
        region_data['count'],
        color=colors,
        zorder = 2
    )
    ax.set_title(region, fontsize=14)
    ax.set_xlabel("")
    ax.set_ylabel("")
    ax.set_xticks(xticks)
    ax.set_xticklabels(xticks, fontsize=10)
    ax.tick_params(axis='y', labelsize=10)
    ax.grid(True, axis="x",which='major', linestyle='--', linewidth=0.5, color='gray', zorder = 1)

for ax in axes.flat[len(regioni):]:
    ax.axis('off')

plt.show()
