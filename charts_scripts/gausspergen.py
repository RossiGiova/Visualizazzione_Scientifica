import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import CubicSpline

# Carica i dati dal file CSV
df = pd.read_csv("data/csv/pokemon_not_complete.csv")

# Definire il range per i valori 'total'
offset = 100
range_values = [f"{x}-{x+offset}" for x in range(100, 750, offset)]

# Ottieni tutte le generazioni presenti nel dataset
generations = df["generation"].unique()
num_generations = len(generations)

# Imposta dimensione griglia per 3x3 layout
rows, cols = 3, 3
fig, axs = plt.subplots(rows, cols, figsize=(15, 15))
axs = axs.flatten()  # Converte la griglia in un array 1D per iterare facilmente

# Loop su ogni generazione per creare un grafico separato
for i, gen in enumerate(generations):
    # Filtra i dati per la generazione corrente
    gen_data = df[df["generation"] == gen]["total"].to_list()

    # Inizializza un dizionario per contare i range di valori
    range_counts = {ranges: 0 for ranges in range_values}
    
    # Conta i valori per ogni range
    for dato in gen_data:
        for text in range_counts.keys():
            min_val, max_val = map(int, text.split("-"))
            if min_val < dato <= max_val:
                range_counts[text] += 1

    # Prepara i dati per il grafico
    x_labels = list(range_counts.keys())
    y_values = list(range_counts.values())
    x_numeric = np.arange(len(x_labels))
    
    # Crea la spline per l'interpolazione
    cs = CubicSpline(x_numeric, y_values)
    x_dense = np.linspace(0, len(x_labels) - 1, 500)
    y_dense = cs(x_dense)
    
    # Plotta i dati e la curva interpolata nel subplot corrispondente
    axs[i].plot(x_dense, y_dense, color='b', label='Curva Interpolata')
    axs[i].plot(x_numeric, y_values, 'bo', label='Dati Originali')
    
    # Aggiungi etichette ai punti
    for j, value in enumerate(y_values):
        axs[i].text(x_numeric[j], value, str(value), ha='center', va='bottom')
    
    # Impostazioni del grafico per la generazione corrente
    #axs[i].set_title(f"Distribuzione dei valori di 'total' - Gen {gen}")
    axs[i].set_xticks(x_numeric)
    axs[i].set_xticklabels(x_labels, rotation=0)
    axs[i].legend()

# Rimuove eventuali subplot vuoti
for j in range(i + 1, rows * cols):
    fig.delaxes(axs[j])

# Imposta etichetta generale per l'asse X e layout generale
plt.tight_layout()
plt.show()
