class Solution {
public:
    int combinationSum4(vector<int>& nums, int target) {
        vector<double> ways;
        ways.resize(target + 1, 0);
        ways[0] = 1;

        for (int base = 0; base < target; base++)
            for (auto c : nums)
                if (ways[base] > 0)
                    if (base + c < ways.size())
                        ways[base + c] += ways[base];

        return ways[target];
    }
};
