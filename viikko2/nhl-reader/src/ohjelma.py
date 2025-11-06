import requests
from player import Player

class PlayerReader:
    def __init__(self, url):
        self.url = url

    def get_players(self):
        response = requests.get(self.url)
        players = response.json()
        return [Player(player_dict) for player_dict in players]

class PlayerStats:
    def __init__(self, reader):
        self.reader = reader

    def top_scorers_by_nationality(self, nationality):
        players = self.reader.get_players()
        players_by_nationality = [
            player for player in players 
            if player.nationality == nationality
        ]
        
        players_by_nationality.sort(
            key=lambda player: player.goals + player.assists,
            reverse=True
        )
        
        return players_by_nationality

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2024-25/players"
    reader = PlayerReader(url)
    stats = PlayerStats(reader)
    players = stats.top_scorers_by_nationality("FIN")

    print("Finnish players:")
    for player in players:
        print(player)

if __name__ == "__main__":
    main()