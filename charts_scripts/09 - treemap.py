import pandas as pd
import matplotlib.pyplot as plt
import squarify

type_colors = {
    "normal": "#A8A878", "fire": "#F08030", "water": "#6890F0", "electric": "#F8D030",
    "grass": "#78C850", "ice": "#98D8D8", "fighting": "#C03028", "poison": "#A040A0",
    "ground": "#E0C068", "flying": "#A890F0", "psychic": "#F85888", "bug": "#A8B820",
    "rock": "#B8A038", "ghost": "#705898", "dragon": "#7038F8", "dark": "#705848",
    "steel": "#B8B8D0", "fairy": "#F0B6BC"
}

def combine_colors(color1, color2):

    if not color2:
        return color1

    c1 = tuple(int(color1.lstrip('#')[i:i+2], 16) for i in (0, 2, 4))
    c2 = tuple(int(color2.lstrip('#')[i:i+2], 16) for i in (0, 2, 4))

    combined = tuple((c1[i] + c2[i]) // 2 for i in range(3))

    return f"#{combined[0]:02X}{combined[1]:02X}{combined[2]:02X}"

csv_file = 'data/csv/pokemon_not_complete.csv'
data = pd.read_csv(csv_file)

# Filtra i Pokémon che hanno un form_type non valido
#data = data[~data["form_type"].isin(["mega", "giga", "archeo", "form"])]

data['type_2'] = data['type_2'].replace("Null", "")

if 'type_1' in data.columns and 'type_2' in data.columns:

    data['type_combination'] = data.apply(
        lambda row: tuple(sorted([row['type_1'], row['type_2'] if row['type_2'] else row['type_1']])),
        axis=1
    )

    type_counts = data['type_combination'].value_counts().reset_index()
    type_counts.columns = ['type_combination', 'count']

    type_counts = type_counts[type_counts['count'] >= 4]

    labels = [
        f"{types[0]} & {types[1]}\n ({count})" if types[0] != types[1] else f"{types[0]}\n ({count})"
        for types, count in zip(type_counts['type_combination'], type_counts['count'])
    ]

    sizes = type_counts['count']

    colors = [
        combine_colors(
            type_colors.get(types[0], "#000000"),
            type_colors.get(types[1], "#000000") if types[0] != types[1] else ""
        )
        for types in type_counts['type_combination']
    ]
    

    plt.figure(figsize=(14, 10))
    squarify.plot(sizes=sizes, label=labels, alpha=0.9, color=colors)
    plt.title('Distribuzione dei Tipi (Minimo 4 Occorrenze)', fontsize=16)
    plt.axis('off')
    plt.tight_layout()
    plt.show()

else:
    print("Le colonne 'type_1' e 'type_2' non sono presenti nel file CSV.")
