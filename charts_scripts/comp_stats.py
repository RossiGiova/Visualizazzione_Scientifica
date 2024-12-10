import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df1 = pd.read_csv('data/csv/pokemon_not_complete.csv')
df2 = pd.read_csv('data/csv/recent_comp.csv')


merged_df = pd.merge(df2, df1, on='pokedex')

comp_stats = merged_df[["hp", "attack", "defense", "special-attack", "special-defense", "speed"]].mean()
all_stats = df1[["hp", "attack", "defense", "special-attack", "special-defense", "speed"]].mean()

stats_comparison = pd.DataFrame({
    'stat': comp_stats.index,
    'comp_stats': comp_stats.values,
    'all_stats': all_stats.values
})

stats_comparison_melted = stats_comparison.melt(id_vars='stat', var_name='stat_group', value_name='value')

plt.figure(figsize=(10, 6))
sns.barplot(x='stat', y='value', hue='stat_group', data=stats_comparison_melted)

plt.title('Comparison of Stats: Comp Stats vs All Stats')
plt.xticks(rotation=45)
plt.tight_layout()

plt.show()
