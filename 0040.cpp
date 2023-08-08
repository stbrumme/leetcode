class Solution {
public:
    vector<vector<int>> combinationSum2(vector<int>& candidates, int target) {
        sort(candidates.begin(), candidates.end());
        map<int, set<multiset<int>>> dp;
        dp[0] = {{}};

        for (auto x : candidates)
        {
            auto next = dp;

            for (auto& level : dp)
                for (auto base : level.second)
                {
                    int sum = 0;
                    for (auto n : base)
                        sum += n;

                    if (sum + x > target)
                        continue;

                    base.insert(x);
                    next[sum + x].insert(move(base));
                }

            dp = move(next);
        }

        vector<vector<int>> result;
        for (auto base : dp[target])
        {
            vector<int> add({ base.begin(), base.end() });
            result.push_back(add);
        }

        return result;
    }
};
