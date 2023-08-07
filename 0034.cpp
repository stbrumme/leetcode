class Solution {
public:
    vector<int> searchRange(vector<int>& nums, int target) {
        auto one = lower_bound(nums.begin(), nums.end(), target);
        auto two = lower_bound(one,          nums.end(), target + 1);

        if (one == nums.end() || *one != target)
            return { -1, -1 };

        return { int(one - nums.begin()), int(two - nums.begin()) - 1 };
    }
};
