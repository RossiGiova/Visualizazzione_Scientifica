import pandas

df = pandas.read_csv("data/csv/pokemon_not_complete.csv")

df = df[df["generation"] == 7]
df1 = df[df["type_1"] == "water"]
df2 = df[df["type_2"] == "water"]

df3 = pandas.concat([df1, df2])

for pokemon in df3["name"]:
    print(pokemon)