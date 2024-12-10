import requests, csv
from bs4 import BeautifulSoup

URL = "https://bulbapedia.bulbagarden.net/wiki/List_of_moves"
page = requests.get(URL)



soup = BeautifulSoup(page.content, "html.parser")
results = soup.find_all("table")[0]
rows = []
for row in results.find_all('tr'):  # Salta l'intestazione
    cols = row.find_all('td')
    row_data = [col.text[:len(col.text)-1] for col in cols]
    rows.append(row_data)

for i, row in enumerate(rows):
    for j, fields in enumerate(row):
        if fields in "\u221e" or fields in " 	∞ " or fields in "\u221e%" or fields in " 	∞ %":
            rows[i][j] = "infinite"
    print(rows[i])


with open("pokemon_move.csv", "w", newline="") as move_csv:
    """csv_writer = csv.writer(move_csv, delimiter=",")
    for i, row in enumerate(rows):
        print(i)
        csv_writer.writerow(row)
    """

    for i, row in enumerate(rows):        
        move_csv.write(", ".join(row))