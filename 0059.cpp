class Solution {
public:
    vector<vector<int>> generateMatrix(int n) {

        if (n == 1)
            return { { 1 }};

        // see problem 54
        vector<vector<int>> result;
        result.resize(n);
        for (auto& r : result)
            r.resize(n, 0);

        int dx = 1;
        int dy = 0;
        int x = 0;
        int y = 0;

        int value = 1;
        while (true)
        {
            if (result[y][x] > 0)
                break;

            result[y][x] = value++;

            x += dx;
            y += dy;

            if (x < 0 || y < 0 || y >= n || x >= n || result[y][x] > 0)
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

