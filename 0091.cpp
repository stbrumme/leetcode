class Solution {
public:
    int numDecodings(string s) {
        map<int, int> dp;
        dp[0] = 1;

        for (int i = 0; i < s.size(); i++)
        {
            auto c = s[i];

            if (c == '0')
            {
                if (i == 0 || s[i-1] == '0' || s[i-1] > '2')
                    return 0;
                dp[i+1] += dp[i-1];
                continue;
            }

            dp[i+1] += dp[i];

            if (i == 0)
                continue;

            if (s[i-1] == '1')
            {
                dp[i+1] += dp[i-1];
                continue;
            }
            if (s[i-1] == '2' && c >= '1' && c <= '6')
            {
                dp[i+1] += dp[i-1];
                continue;
            }
        }

        return dp[s.size()];
    }
};
