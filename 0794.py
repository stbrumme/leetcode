class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:
        o = 0
        x = 0
        for row in board:
            for r in row:
                if   r == "O":
                    o += 1
                elif r == "X":
                    x += 1
                elif r != " ":
                    return False

        # X starts
        if x != o and x != o + 1:
            return False

        def won(player):
            # vertical + horizontal
            for i in range(3):
                if board[i][0] == player and board[i][1] == player and board[i][2] == player:
                    return True
                if board[0][i] == player and board[1][i] == player and board[2][i] == player:
                    return True

            # diagonals
            if board[0][0] == player and board[1][1] == player and board[2][2] == player:
                return True
            if board[2][0] == player and board[1][1] == player and board[0][2] == player:
                return True

            return False

        # X can't have a triple if it's X's turn
        if x == o:
            if won("X"):
                return False
        # O can't have a triple if it's O's turn
        if x == o + 1:
            if won("O"):
                return False

        # both can't win at the same time
        if won("X") and won("O"):
            return False

        return True
