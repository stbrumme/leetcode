class Solution {
public:
    void rotate(vector<vector<int>>& matrix) {
        int size = matrix.size();
        int m    = size - 1;
        for (int x = 0; x < (size+1)/2; x++)
            for (int y = 0; y < size/2; y++)
            {
                int tmp = matrix[x][y];
                matrix[  x][  y] = matrix[m-y][  x];
                matrix[m-y][  x] = matrix[m-x][m-y];
                matrix[m-x][m-y] = matrix[  y][m-x];
                matrix[  y][m-x] = tmp;
            }
    }
};
