class Solution {
public:
    int maximalSquare(vector<vector<char>>& matrix) {
        int h = matrix.size();
        int w = matrix[0].size();
        vector<vector<int>> rightOnes;
        rightOnes.resize(h);
        for (auto& r : rightOnes)
            r.resize(w);

        for (int y = 0; y < h; y++)
            for (int x = 0; x < w; x++)
            {
                if (matrix[y][x] == '0')
                {
                    rightOnes[y][x] = 0;
                    continue;
                }

                if (x > 0 && rightOnes[y][x-1] > 0)
                {
                    rightOnes[y][x] = rightOnes[y][x-1] - 1;
                    continue;
                }

                int z = 0;
                for (; x+z < w && matrix[y][x+z] == '1'; z++)
                    ;
                rightOnes[y][x] = z;
            }

        int maxx = 0;
        for (int y = 0; y < h; y++)
            for (int x = 0; x < w; x++)
            {
                if (rightOnes[y][x] == 0)
                    continue;

                int maxRight = rightOnes[y][x];
                for (int i = 0; i+y < h; i++)
                {
                    if (maxRight > rightOnes[y+i][x])
                        maxRight = rightOnes[y+i][x];

                    if (maxRight == 0)
                        break;

                    int area = i < maxRight ? (i+1)*(i+1) : maxRight*maxRight;
                    if (maxx < area)
                        maxx = area;

                    if (i >= maxRight)
                        break;
                }
            }

        return maxx;
    }
};
