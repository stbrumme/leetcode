class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        for (int x = 0; x < 9; x++)
            for (int y = 0; y < 9; y++)
            {
                auto current = board[x][y];
                if (current == '.')
                    continue;

                for (int xx = x+1; xx < 9; xx++)
                    if (current == board[xx][y])
                        return false;
                for (int yy = y+1; yy < 9; yy++)
                    if (current == board[x][yy])
                        return false;

                int xx = (x/3)*3;
                int yy = (y/3)*3;
                for (int i = 0; i < 3; i++)
                    for (int j = 0; j < 3; j++)
                    {
                        if (xx + i == x && yy + j == y)
                            continue;
                        if (current == board[xx+i][yy+j])
                            return false;
                    }

            }
        return true;
    }
};
