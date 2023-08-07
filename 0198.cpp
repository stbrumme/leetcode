class Solution {
    map<int, int> cache;
    int dp(vector<int>& nums, int next)
    {
        if (next >= nums.size())
            return 0;

        if (cache.count(next) > 0)
            return cache[next];

        int best = 0;
        for (int i = next; i < nums.size(); i++)
        {
            auto current = nums[i] + dp(nums, i + 2);
            if (best < current)
                best = current;
        }

        cache[next] = best;
        return best;
    }

public:
    int rob(vector<int>& nums) {
        cache.clear();

        return dp(nums, 0);
    }
};
