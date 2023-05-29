from games.complete_2x2_matrix_game import Complete2by2MatrixGame


class ChickenGame(Complete2by2MatrixGame):
    def __init__(self, num_rounds=1000, player_data=[], player_types=[], permissions_map={}, game_turn_timeout=1, game_name=None, invalid_move_penalty=0):
        super().__init__(num_rounds, player_data,
                         player_types, permissions_map, game_turn_timeout, game_name, invalid_move_penalty)
        self.valid_actions = [0, 1]
        self.utils = [[(0, 0), (-1, 1)],
                      [(1, -1), (-5, -5)]]