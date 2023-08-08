class Solution {
public:
    int coinChange(vector<int>& coins, int amount) {
        vector<int64_t> dp(11000, -1);
        dp[0] = 0;

        for (int64_t i = 0; i <= amount; i++)
        {
            if (dp[i] == -1)
                continue;

            for (auto c : coins)
            {
                int64_t sum = i + c;
                if (sum > amount)
                    continue;

                if (dp[sum] == -1)
                    dp[sum] = dp[i] + 1;
                else
                    dp[sum] = min(dp[sum], dp[i] + 1);
            }
        }

        return dp[amount];
    }
};
