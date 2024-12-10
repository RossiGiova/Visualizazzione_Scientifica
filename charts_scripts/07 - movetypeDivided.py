import pandas as pd
import matplotlib.pyplot as plt

file_path = "data/csv/complete_moves.csv"
df = pd.read_csv(file_path)

type_counts = df['Type'].value_counts()

type_order = type_counts.index
df['Type'] = pd.Categorical(df['Type'], categories=type_order, ordered=True)

type_category_counts = df.groupby(['Type', 'Category']).size().unstack(fill_value=0).reindex(type_order)

category_colors = {
    'Physical': '#fd8d3c', #'#FF9636',  # Rosa pallido
    'Special': '#6baed6',#'#0BB7FE',  # Azzurro chiaro
    'Status': '#a1d99b'#'#81B622'    # Verde chiaro
}

type_category_counts.plot(kind='barh', stacked=True, figsize=(12, 6), color=category_colors, zorder=2)

plt.title("Numero di Mosse per Tipo di Pokémon e Categoria", fontsize=14)

plt.legend(title="Categoria", fontsize=10)

plt.grid(axis="x", zorder=0)

ax = plt.gca()
ax.set_ylabel("")

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.tight_layout()
plt.show()
