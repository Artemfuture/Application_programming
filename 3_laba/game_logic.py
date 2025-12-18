class GameLogic:
    def __init__(self):
        self.reset_game()
        self.player_x_score = 0
        self.player_o_score = 0
        self.draws = 0

    def reset_game(self):
        self.game_board = [["" for i in range(3)] for j in range(3)]
        self.current_player = "X"
        self.game_over = False
        self.winning_cells = []

    def make_move(self, row, col):
        if self.game_over or self.game_board[row][col] != "":
            return False, "continue", None

        self.game_board[row][col] = self.current_player

        if self.check_winner():
            self.game_over = True
            if self.current_player == "X":
                self.player_x_score += 1
            else:
                self.player_o_score += 1
            return True, "win", self.current_player

        if self.is_board_full():
            self.game_over = True
            self.draws += 1
            return True, "draw", None
        return True, "continue", None

    def check_winner(self) -> bool:
        result = False
        self.winning_cells = []
        for i in range(3):
            if (
                self.game_board[i][0]
                == self.game_board[i][1]
                == self.game_board[i][2]
                != ""
            ):
                self.winning_cells = [(i, 0), (i, 1), (i, 2)]
                result = True

        for i in range(3):
            if (
                self.game_board[0][i]
                == self.game_board[1][i]
                == self.game_board[2][i]
                != ""
            ):
                self.winning_cells = [(0, i), (1, i), (2, i)]
                result = True

        if (
            self.game_board[0][0]
            == self.game_board[1][1]
            == self.game_board[2][2]
            != ""
        ):
            self.winning_cells = [(0, 0), (1, 1), (2, 2)]
            result = True

        if (
            self.game_board[0][2]
            == self.game_board[1][1]
            == self.game_board[2][0]
            != ""
        ):
            self.winning_cells = [(0, 2), (1, 1), (2, 0)]
            result = True

        return result

    def is_board_full(self) -> bool:
        result = True
        for row in self.game_board:
            for cell in row:
                if cell == "":
                    result = False
                    break
        return result

    def reset_score(self):
        self.player_x_score = 0
        self.player_o_score = 0
        self.draws = 0

    def get_score_text(self):
        return f"   X:{self.player_x_score}    O:{self.player_o_score}     Ничьи:{self.draws}"
