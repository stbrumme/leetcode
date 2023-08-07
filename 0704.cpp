class Solution {
public:
    int search(vector<int>& nums, int target) {
        auto i = lower_bound(nums.begin(), nums.end(), target);

        if (i == nums.end())
            return -1;

        if (*i == target)
            return i - nums.begin();

        return -1;
    }
};
