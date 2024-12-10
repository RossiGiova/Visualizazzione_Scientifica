import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/csv/pokemon_complete.csv")

df = df[df["form_type"] != "mega"]
df = df[df["form_type"] != "giga"]
df = df[df["form_type"] != "archeo"]
df = df[df["form_type"] != "form"]

nomi = ["Kanto", "Johto", "Hoenn", "Sinnoh", "Unima", "Kalos", "Alola", "Galar", "Paldea"]
dati = {}
for i, regioni in enumerate(df['generation'].value_counts().sort_index()):
    dati[nomi[i]] = regioni

print(df['generation'].value_counts().sort_index())

plt.figure(figsize=(10, 6))
plt.barh(list(dati.keys())[::-1], list(dati.values())[::-1], color='skyblue', zorder=2)


ax = plt.gca()
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(True)
ax.spines['bottom'].set_visible(True)


plt.grid(axis="x", zorder=1)


plt.title("Distribuzione dei Pokémon per Regione")
plt.show()
