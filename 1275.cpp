class Solution {
public:
    string tictactoe(vector<vector<int>>& moves) {
        char board[3][3] = { { ' ', ' ', ' ' }, { ' ', ' ', ' ' }, { ' ', ' ', ' ' }};
        for (auto i = 0; i < moves.size(); i++)
        {
            auto r = moves[i][0];
            auto c = moves[i][1];
            board[r][c] = (i & 1) ? 'B' : 'A';
        }

        for (int i = 0; i < 3; i++)
        {
            if (board[i][0] != ' ' && board[i][0] == board[i][1] && board[i][0] == board[i][2])
                return string(1, board[i][0]);
            if (board[0][i] != ' ' && board[0][i] == board[1][i] && board[0][i] == board[2][i])
                return string(1, board[0][i]);
            if (board[0][0] != ' ' && board[0][0] == board[1][1] && board[0][0] == board[2][2])
                return string(1, board[0][0]);
            if (board[0][2] != ' ' && board[0][2] == board[1][1] && board[0][2] == board[2][0])
                return string(1, board[0][2]);
        }

        if (moves.size() == 9)
            return "Draw";

        return "Pending";
    }
};
