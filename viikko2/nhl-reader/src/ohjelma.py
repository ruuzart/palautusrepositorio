import argparse
import requests
from player import Player

class PlayerReader:
    def __init__(self, season):
        self.season = season
        self.url = f"https://studies.cs.helsinki.fi/nhlstats/{season}/players"

    def get_players(self):
        response = requests.get(self.url, timeout=5)
        players = response.json()
        return [Player(player_dict) for player_dict in players]

    def test_connection(self):
        """Test the connection to the NHL stats service"""
        try:
            requests.get(self.url, timeout=5)
            return True
        except requests.RequestException:
            return False

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

    def list_nationalities(self):
        """Returns a sorted list of all unique nationalities in the data"""
        players = self.reader.get_players()
        return sorted(list(set(player.nationality for player in players)))

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--nationality", default="FIN",
                      help="nationality of players (e.g. FIN, SWE, CAN)")
    parser.add_argument("--season", default="2024-25",
                      help="season in format YYYY-YY (e.g. 2024-25)")

    args = parser.parse_args()

    reader = PlayerReader(args.season)
    stats = PlayerStats(reader)
    players = stats.top_scorers_by_nationality(args.nationality)

    for player in players:
        print(player)

if __name__ == "__main__":
    main()
