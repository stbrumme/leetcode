class Solution {
public:
    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        unordered_map<int, set<multiset<int>>> dp;

        sort(candidates.begin(), candidates.end());

        dp[0].insert({{}});

        for (int i = 0; i < target; i++)
        {
            for (const auto& base : dp[i])
            {
                auto sum = 0;
                for (auto x : base)
                    sum += x;

                int prev = -1;
                for (auto x : candidates)
                {
                    if (sum + x > target)
                        break;

                    if (x == prev)
                        continue;
                    prev = x;

                    auto next = base;
                    next.insert(x);
                    dp[sum + x].insert(next);
                }
            }
        }

        vector<vector<int>> result;
        for (auto& base : dp[target])
            result.push_back({base.begin(), base.end()});

        return result;
    }
};
