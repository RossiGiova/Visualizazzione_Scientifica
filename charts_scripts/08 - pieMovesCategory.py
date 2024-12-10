import pandas as pd
import matplotlib.pyplot as plt

file_path = "data/csv/complete_moves.csv"
df = pd.read_csv(file_path)

category_counts = df['Category'].value_counts()
category_counts.sort_values()

plt.figure(figsize=(10, 10))
plt.pie(
    category_counts, 
    labels=category_counts.index, 
    autopct='%1.1f%%', 
    startangle=90, 
    colors=[ '#fd8d3c','#a1d99b','#6baed6',],
    textprops={'fontsize': 14} 
)
plt.title("Distribuzione delle Mosse Pokémon tra le Categorie", fontsize=16)
plt.show()
