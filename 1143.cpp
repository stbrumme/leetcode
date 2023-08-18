class Solution {
public:
    int longestCommonSubsequence(string text1, string text2) {
        auto width  = text1.size();
        auto height = text2.size();

        vector<vector<short>> ops(width + 1);
        for (auto& o : ops)
            o.resize(height + 1, 0);

        // similar to edit distance
        for (int i = 0; i < width; i++)
            for (int j = 0; j < height; j++)
                if (text1[i] == text2[j])
                    ops[i+1][j+1] = ops[i][j] + 1; // even longer
                else
                    ops[i+1][j+1] = max(ops[i+1][j], ops[i][j+1]); // nope, not better

        return ops[width][height];
    }
};
