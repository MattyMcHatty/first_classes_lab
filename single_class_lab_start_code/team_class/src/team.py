class Team:
    def __init__(self, name, players, coach):
        self.name = name
        self.players = players
        self.coach = coach
        self.points = 0

    def add_player(self, new_player_name):
        self.players.append(new_player_name)

    def has_player(self, player_name_to_find):
        found_it= False
        for player in self.players:
            if player == player_name_to_find:
                found_it= True
        
        return found_it

    def play_game(self, have_won_game):
        if have_won_game:
            self.points += 3