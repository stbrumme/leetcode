class Solution {
public:
    int kthLargestValue(vector<vector<int>>& matrix, int k) {
        auto exclusive = matrix;
        // upper and left border
        for (auto y = 1; y < exclusive.size(); y++)
            exclusive[y][0] ^= exclusive[y - 1][0];
        for (auto x = 1; x < exclusive[0].size(); x++)
            exclusive[0][x] ^= exclusive[0][x - 1];

        std::vector<int> all;
        for (auto y = 0; y < exclusive.size(); y++)
            for (auto x = 0; x < exclusive[y].size(); x++)
            {
                if (x > 0 && y > 0)
                    // the hardest part of this problem was figuring out the third term ...
                    exclusive[y][x] ^= exclusive[y - 1][x] ^ exclusive[y][x - 1] ^ exclusive[y - 1][x - 1];
                all.push_back(exclusive[y][x]);
            }

        auto smallest = all.size() - k;
        // partial sort
        nth_element(all.begin(), all.begin() + smallest, all.end());
        return all[smallest];
    }
};
