import os
import pandas as pd
import plotly.express as px

percorso = "data/csv/tournaments"

print(len(os.listdir(percorso)))

all_nationality = {}

for file in os.listdir(percorso):
    df = pd.read_csv(f"{percorso}/{file}")
    new_dict = df["Nazionalità"].value_counts(dropna=False).to_dict()
    for key, value in new_dict.items():
        all_nationality[key] = all_nationality.get(key, 0) + value


df = pd.DataFrame(list(all_nationality.items()), columns=['country', 'players'])

fig = px.choropleth(
    df,
    locations="country",
    locationmode="country names",
    color="players",  
    title="Heatmap Giocatori Pokémon per Nazionalità",
    color_continuous_scale="RdYlGn_r"
)

fig.show()