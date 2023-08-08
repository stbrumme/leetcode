class Solution {
public:
    int firstMissingPositive(vector<int>& nums) {
        // n log n
        sort(nums.begin(), nums.end());
        auto last = unique(nums.begin(), nums.end());
        nums.erase(last, nums.end());

        auto pos = upper_bound(nums.begin(), nums.end(), 0);

        int result = 1;
        while (pos != nums.end() && *pos == result)
        {
            pos++;
            result++;
        }

        return result;
    }
};
