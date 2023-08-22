class Solution {
public:
    void gameOfLife(vector<vector<int>>& board) {
        int width  = board.size();
        int height = board[0].size();

        vector<vector<int>> next(width, vector<int>(height, 0));
        for (int x = 0; x < width; x++)
            for (int y = 0; y < height; y++)
            {
                int neighbors = 0;
                if (x > 0 && y > 0)
                    neighbors += board[x-1][y-1];
                if (x > 0)
                    neighbors += board[x-1][y];
                if (x > 0 && y < height - 1)
                    neighbors += board[x-1][y+1];
                if (y > 0)
                    neighbors += board[x][y-1];
                if (y < height - 1)
                    neighbors += board[x][y+1];
                if (x < width - 1 && y > 0)
                    neighbors += board[x+1][y-1];
                if (x < width - 1)
                    neighbors += board[x+1][y];
                if (x < width - 1 && y < height - 1)
                    neighbors += board[x+1][y+1];

                if (board[x][y] == 0)
                {
                    if (neighbors == 3)
                        next[x][y] = 1;
                }
                else
                {
                    if (neighbors == 2 || neighbors == 3)
                        next[x][y] = 1;
                }
            }

        board = next;
    }
};
