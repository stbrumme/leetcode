class Solution {
public:
    int orangesRotting(vector<vector<int>>& grid) {
        int w = grid.size();
        int h = grid[0].size();

        int result = 0;
        for (; ; result++)
        {
            int newRotten = 0;
            int numFresh = 0;
            auto next = grid;

            for (int x = 0; x < w; x++)
                for (int y = 0; y < h; y++)
                {
                    if (grid[x][y] != 1)
                        continue;

                    bool rot = false;
                    if (x > 0 && grid[x-1][y] == 2)
                        rot = true;
                    if (y > 0 && grid[x][y-1] == 2)
                        rot = true;
                    if (x < w-1 && grid[x+1][y] == 2)
                        rot = true;
                    if (y < h-1 && grid[x][y+1] == 2)
                        rot = true;

                    if (rot)
                    {
                        newRotten++;
                        next[x][y] = 2;
                    }
                    else
                        numFresh++;
                }

            if (numFresh == 0)
            {
                if (newRotten > 0)
                    result++;
                break;
            }
            if (newRotten == 0)
                return -1;

            grid = next;
        }

        return result;
    }
};

