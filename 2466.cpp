class Solution {
public:
    int countGoodStrings(int low, int high, int zero, int one) {
        vector<int> dp(high + 1, 0);
        dp[0] = 1;

        const int MOD = 1000000007;

        for (int i = 0; i < high; i++)
        {
            if (dp[i] == 0)
                continue;

            if (i + zero <= high)
            {
                dp[i + zero] += dp[i];
                dp[i + zero] %= MOD;
            }

            if (i + one <= high)
            {
                dp[i + one] += dp[i];
                dp[i + one] %= MOD;
            }
        }

        int64_t sum = 0;
        for (int i = low; i <= high; i++)
            sum += dp[i];

        return sum % MOD;
    }
};
