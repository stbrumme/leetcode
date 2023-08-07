class Solution {
public:
    int uniquePathsWithObstacles(vector<vector<int>>& obstacleGrid) {
        if (obstacleGrid[0][0] == 1)
            return 0;

        int w = obstacleGrid.size();
        int h = obstacleGrid[0].size();

        vector<vector<int>> board;
        board.resize(w);
        for (auto& b : board)
            b.resize(h, 0);

        board[0][0] = 1;

        for (int x = 0; x < w; x++)
            for (int y = 0; y < h; y++)
            {
                if (obstacleGrid[x][y] == 1)
                    continue;

                if (x > 0 && obstacleGrid[x-1][y] == 0)
                    board[x][y] += board[x-1][y];
                if (y > 0 && obstacleGrid[x][y-1] == 0)
                    board[x][y] += board[x][y-1];
            }

        return board[w-1][h-1];
    }
};
