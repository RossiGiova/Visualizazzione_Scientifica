import pandas as pd
import matplotlib.pyplot as plt

file_name = "data/csv/revenues.csv"
df = pd.read_csv(file_name)

df_sorted = df.sort_values(by="Gross revenue (est.)", ascending=True)

plt.figure(figsize=(10, 6))
plt.grid(axis="x", zorder=1)
plt.barh(df_sorted["Media"], df_sorted["Gross revenue (est.)"] / 1e9, color='skyblue', zorder=2)
plt.title("entrate lorde dai prodotti pokemon (in trilioni)")
plt.tight_layout()
plt.show()
