class Solution {
public:
    int maxSumSubmatrix(vector<vector<int>>& matrix, int k)
    {
        auto result = std::numeric_limits<int>::min();
        auto height = matrix.size();
        auto width  = matrix[0].size();

        // one row and one column larger than matrix to simplify inner loops
        std::vector<std::vector<int>> prefix(height + 1, std::vector<int>(width + 1, 0));

        // compute prefix sum
        for (size_t y = 1; y <= height; y++)
            for (size_t x = 1; x <= width; x++)
            {
                prefix[y][x]  = matrix[y - 1][x - 1];
                prefix[y][x] += prefix[y][x - 1];
                prefix[y][x] += prefix[y - 1][x];
                prefix[y][x] -= prefix[y - 1][x - 1];
            }

        // brute force: iterate over all rectangles
        // this approach is too slow in Python but actually feasible in C++
        for (size_t y = 1; y <= height; y++)
            for (size_t x = 1; x <= width; x++)
                for (int y2 = 0; y2 < int(y); y2++)
                    for (int x2 = 0; x2 < int(x); x2++)
                    {
                        int rectangle = prefix[y][x];
                        rectangle    -= prefix[y][x2];
                        rectangle    -= prefix[y2][x];
                        rectangle    += prefix[y2][x2];

                        // even better rectangle found
                        if (result < rectangle && rectangle <= k)
                        {
                            result = rectangle;
                            // early exit
                            if (result == k)
                                return result;
                        }
                    }

        return result;
    }
};
