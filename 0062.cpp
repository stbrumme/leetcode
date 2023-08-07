class Solution {
public:
    int uniquePaths(int m, int n) {
        vector<vector<int>> board;
        board.resize(m);
        for (auto& b : board)
            b.resize(n);

        board[0][0] = 1;

        for (int x = 0; x < m; x++)
            for (int y = 0; y < n; y++)
            {
                if (x > 0)
                    board[x][y] += board[x-1][y];
                if (y > 0)
                    board[x][y] += board[x][y-1];
            }

        return board[m-1][n-1];
    }
};
