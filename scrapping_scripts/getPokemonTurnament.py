import requests
import csv
from bs4 import BeautifulSoup

for i in range(295, 364):
    print(i)
    URL = f"https://limitlessvgc.com/events/{i}/"
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, "html.parser")
    try:
        results = soup.find_all("table")[0]
    except:
        continue

    filename = f"data/csv/tournaments/{i}.csv"
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)

        writer.writerow(["Posizione", "ID_Giocatore", "Nome_Giocatore", "Nazionalità", "Team_Pokémon"])

        for row in results.find_all('tr')[1:]:
            fields = row.find_all('td')
            
            if len(fields) < 5:
                continue

            posizione = fields[0].text.strip()

            player_link = fields[1].find('a')
            id_giocatore = player_link['href'].split('/')[-1]
            nome_giocatore = player_link.text.strip()

            nazionalita_tag = fields[2].find('img')
            nazionalita = nazionalita_tag['alt'] if nazionalita_tag else "N/A"

            team_div = fields[3].find('div', class_='vgc-team')
            pokemon_team = []
            if team_div:
                pokemon_tags = team_div.find_all('span', class_='tt')
                pokemon_team = [tag['title'] for tag in pokemon_tags if 'title' in tag.attrs]

            writer.writerow([posizione, id_giocatore, nome_giocatore, nazionalita, ", ".join(pokemon_team)])

    print(f"I dati sono stati salvati con successo nel file {filename}.")
