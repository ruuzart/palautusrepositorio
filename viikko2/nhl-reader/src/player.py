class Player:
    def __init__(self, player_dict):
        self.name = player_dict['name']
        self.nationality = player_dict['nationality']
        self.assists = player_dict['assists']
        self.goals = player_dict['goals']
        self.team = player_dict['team']

    def __str__(self):
        return f"{self.name:20} {self.team:4} {self.goals:2} + {self.assists:2} = {self.goals + self.assists:2}"

    def get_points(self):
        """Returns the total points (goals + assists) for the player"""
        return self.goals + self.assists
