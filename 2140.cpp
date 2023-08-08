class Solution {
public:
    long long mostPoints(vector<vector<int>>& questions) {
        vector<int64_t> dp(questions.size() + 1, 0);

        int64_t best = 0;
        for (int i = 0; i < questions.size(); i++)
        {
            auto brain = questions[i][0];
            auto skip  = questions[i][1];

            auto sum = dp[i] + brain;

            auto next = i + skip + 1;
            if (next < questions.size())
                dp[next] = max(dp[next], sum);

            if (best < sum)
                best = sum;

            // skip
            dp[i + 1] = max(dp[i], dp[i+1]);
        }

        return best;
    }
};
