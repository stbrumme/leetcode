class Solution {
public:
    void setZeroes(vector<vector<int>>& matrix) {
        set<int> clearX, clearY;
        for (int x = 0; x < matrix.size(); x++)
            for (int y = 0; y < matrix[x].size(); y++)
                if (matrix[x][y] == 0)
                {
                    clearX.insert(x);
                    clearY.insert(y);
                }

        for (auto x : clearX)
            for (int y = 0; y < matrix[x].size(); y++)
                matrix[x][y] = 0;

        for (auto y : clearY)
            for (int x = 0; x < matrix.size(); x++)
                matrix[x][y] = 0;
    }
};
