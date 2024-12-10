import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline

csv_file = 'data/csv/complete_moves.csv'
data = pd.read_csv(csv_file)

if 'Power' in data.columns:

    power_values = pd.to_numeric(data['Power'], errors='coerce')
    power_values = power_values.replace([np.inf, -np.inf], np.nan)
    power_values = power_values.dropna()

    frequency = power_values.value_counts().sort_index()

    x = frequency.index
    y = frequency.values
    x_new = np.linspace(x.min(), x.max(), 500)
    spline = make_interp_spline(x, y, k=3)
    y_smooth = spline(x_new)

    plt.figure(figsize=(10, 6))
    plt.plot(x_new, y_smooth, color='red', label='Interpolazione', linewidth=2)
    plt.scatter(x, y, color='blue', alpha=0.7, label='Dati originali')
    plt.title('Distribuzione dei Valori di Power con Interpolazione')
    plt.xlabel('Valore di Power')
    plt.ylabel('Frequenza')
    plt.grid(True)
    plt.legend()
    plt.show()
else:
    print("Il campo 'Power' non è presente nel file CSV.")