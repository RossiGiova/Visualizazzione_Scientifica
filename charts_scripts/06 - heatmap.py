
#COMPLETOO!!!

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

types = [
    "Normale", "Fuoco", "Acqua", "Elettro","Erba", "Ghiaccio", "Lotta", 
    "Veleno", "Terra", "Volante", "Psico", "Coleottero", "Roccia", 
    "Spettro", "Drago", "Buio", "Acciaio", "Folletto"
]

# 2.0 = superefficace, 1.0 = normale, 0.5 = non molto efficace, 0 = nessun effetto

table = [
    [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.5, 0.0, 1.0, 1.0, 0.5, 1.0,],
    [1.0, 0.5, 0.5, 1.0, 2.0, 2.0, 1.0, 1.0, 1.0, 1.0, 1.0, 2.0, 0.5, 1.0, 0.5, 1.0, 2.0, 1.0,],
    [1.0, 2.0, 0.5, 1.0, 0.5, 1.0, 1.0, 1.0, 2.0, 1.0, 1.0, 1.0, 2.0, 1.0, 0.5, 1.0, 1.0, 1.0,],
    [1.0, 1.0, 2.0, 0.5, 0.5, 1.0, 1.0, 1.0, 0.0, 2.0, 1.0, 1.0, 1.0, 1.0, 0.5, 1.0, 1.0, 1.0,],
    [1.0, 0.5, 2.0, 1.0, 0.5, 1.0, 1.0, 0.5, 2.0, 0.5, 1.0, 0.5, 2.0, 1.0, 0.5, 1.0, 0.5, 1.0,],
    [1.0, 0.5, 0.5, 1.0, 2.0, 0.5, 1.0, 1.0, 2.0, 2.0, 1.0, 1.0, 1.0, 1.0, 2.0, 1.0, 0.5, 1.0,],
    [2.0, 1.0, 1.0, 1.0, 1.0, 2.0, 1.0, 0.5, 1.0, 0.5, 0.5, 0.5, 2.0, 0.0, 1.0, 2.0, 2.0, 0.5,],
    [1.0, 1.0, 1.0, 1.0, 2.0, 1.0, 1.0, 0.5, 0.5, 1.0, 1.0, 1.0, 0.5, 0.5, 1.0, 1.0, 0.0, 2.0,],
    [1.0, 2.0, 1.0, 2.0, 0.5, 1.0, 1.0, 2.0, 1.0, 0.0, 1.0, 0.5, 2.0, 1.0, 1.0, 1.0, 2.0, 1.0,],
    [1.0, 1.0, 1.0, 0.5, 2.0, 1.0, 2.0, 1.0, 1.0, 1.0, 1.0, 2.0, 0.5, 1.0, 1.0, 1.0, 0.5, 1.0,],
    [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 2.0, 2.0, 1.0, 1.0, 0.5, 1.0, 1.0, 1.0, 1.0, 0.0, 0.5, 1.0,],
    [1.0, 0.5, 1.0, 1.0, 2.0, 1.0, 0.5, 0.5, 1.0, 0.5, 2.0, 1.0, 1.0, 0.5, 1.0, 2.0, 0.5, 0.5,],
    [1.0, 2.0, 1.0, 1.0, 1.0, 2.0, 0.5, 1.0, 0.5, 2.0, 1.0, 2.0, 1.0, 1.0, 1.0, 1.0, 0.5, 1.0,],
    [0.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 2.0, 1.0, 1.0, 2.0, 1.0, 0.5, 1.0, 1.0,],
    [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 2.0, 1.0, 0.5, 0.0,],
    [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.5, 1.0, 1.0, 1.0, 2.0, 1.0, 1.0, 2.0, 1.0, 0.5, 1.0, 0.5,],
    [1.0, 0.5, 0.5, 0.5, 1.0, 2.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 2.0, 1.0, 1.0, 1.0, 0.5, 2.0,],
    [1.0, 0.5, 1.0, 1.0, 1.0, 1.0, 2.0, 0.5, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 2.0, 2.0, 0.5, 1.0,],
]


efficacy_matrix = np.array(table)
df = pd.DataFrame(efficacy_matrix, index=types[:len(efficacy_matrix)], columns=types[:len(efficacy_matrix)])

fig, ax = plt.subplots(figsize=(18, 10))
cax = ax.matshow(df, cmap="RdYlGn", alpha=0.80, vmin=0, vmax=2.0)

ax.set_aspect(aspect='auto')
ax.set_box_aspect(0.6)

ax.xaxis.set_label_position('bottom')
ax.xaxis.tick_bottom()

ax.set_xticks(np.arange(len(types[:len(efficacy_matrix)])))
ax.set_yticks(np.arange(len(types[:len(efficacy_matrix)])))
ax.set_xticklabels(types[:len(efficacy_matrix)], rotation=0)
ax.set_yticklabels(types[:len(efficacy_matrix)])

for i in range(len(df.index)):
    for j in range(len(df.columns)):
        ax.text(j, i, f"{df.iloc[i, j]:.1f}", ha='center', va='center', color='black')

legend_labels = {
    0: "Inefficace", 
    0.5: "Poco efficace", 
    1.0: "Normale", 
    2.0: "Superefficace"
}
colors = [cax.cmap(cax.norm(value)) for value in legend_labels.keys()]
patches = [mpatches.Patch(color=colors[i], label=f"{v}") for i, v in enumerate(legend_labels.values())]
plt.legend(handles=patches, title="Efficacia", bbox_to_anchor=(1.05, 0.5), loc='center left')

ax.set_title("Matrice di Efficacia dei Tipi Pokémon", pad=20)
ax.set_xlabel("Tipo Difensore", labelpad=30)
ax.set_ylabel("Tipo Attaccante", rotation=0, labelpad=30)

plt.show()
