class LeagueTable:
    def __init__(self, players):
        self.standings = {player: {'score': 0, 'games': 0} for player in players}

    def record_result(self, player, score):
        self.standings[player]['score'] += score
        self.standings[player]['games'] += 1

    def sorting_func(self, player):
        score_order = self.standings[player]['score'] - self.standings[player]['score']
        if score_order == 0:
            games_order = self.standings[player]['games'] - self.standings[player]['games']
            if games_order == 0:
                return player
        else:
            return score_order

    def player_rank(self, rank):
        players = sorted(self.standings, key=self.sorting_func)
        return players[rank - 1]

if __name__ == '__main__':
    # Example usage
    table = LeagueTable(['Mike', 'Chris', 'Arnold'])
    table.record_result('Mike', 2)
    table.record_result('Mike', 3)
    table.record_result('Arnold', 5)
    table.record_result('Chris', 5)
    print(table.player_rank(1))  # Expected output: Arnold or Chris, depending on the sorting of names since they have the same score and games played.
