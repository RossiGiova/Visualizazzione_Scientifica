import pandas

df = pandas.read_csv("data/csv/complete_moves.csv")
"""
df = df[df["Category"] != "???"]

print(len(df))
"""

df.drop(columns=['#']).to_csv("data/csv/complete_moves.csv")