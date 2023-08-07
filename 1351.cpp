class Solution {
public:
    int countNegatives(vector<vector<int>>& grid) {
        int result = 0;
        for (int x = 0; x < grid.size(); x++)
            for (int y = 0; y < grid[x].size(); y++)
            {
                if (grid[x][y] >= 0)
                    continue;

                result += grid[x].size() - y;
                break;
            }

        return result;
    }
};
