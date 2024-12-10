import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import networkx as nx

types = ["Acqua", "Fuoco", "Erba"]

table = [
    [0.5, 2.0, 0.5],  # Acqua
    [0.5, 0.5, 2.0],  # Fuoco
    [2.0, 0.5, 0.5],  # Erba
]

efficacy_matrix = np.array(table)
df = pd.DataFrame(efficacy_matrix, index=types, columns=types)

G = nx.DiGraph()

for i, att_type in enumerate(types):
    for j, def_type in enumerate(types):
        efficacy = df.iloc[i, j]
        if efficacy == 2.0:  # Aggiungi solo gli archi super efficaci
            G.add_edge(att_type, def_type, weight=efficacy)

plt.figure(figsize=(8, 6))

pos = nx.shell_layout(G)

nx.draw(
    G, pos, with_labels=True,
    node_size=3000, node_color='lightblue',
    font_size=10, font_weight='bold',
    edge_color='#519877', width=2, arrows=True
)

# Legenda per solo super efficace
legend_patches = [mpatches.Patch(color='#519877', label="Superefficace")]
plt.legend(handles=legend_patches, title="Efficacia")

# Mostra il grafico
plt.title("Interazioni Superefficaci tra Acqua, Fuoco ed Erba")
plt.show()
