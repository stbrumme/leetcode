class Solution {
public:
    vector<int> spiralOrder(vector<vector<int>>& matrix) {
        int size = matrix.size() * matrix[0].size();

        vector<int> result;
        result.reserve(size);

        int STOP = 9999;

        int dx = 1;
        int dy = 0;
        int x = 0;
        int y = 0;
        while (result.size() < size)
        {
            result.push_back(matrix[y][x]);
            matrix[y][x] = STOP;
            x += dx;
            y += dy;

            if (x < 0 || y < 0 || y >= matrix.size() || x >= matrix[0].size() || matrix[y][x] == STOP)
            {
                x -= dx;
                y -= dy;
                if      (dx == +1) { dx = 0; dy = +1; }
                else if (dx == -1) { dx = 0; dy = -1; }
                else if (dy == +1) { dx = -1; dy = 0; }
                else               { dx = +1; dy = 0; }
                x += dx;
                y += dy;
            }
        }

        return result;
    }
};
