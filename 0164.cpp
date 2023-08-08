class Solution {
public:
    int maximumGap(vector<int>& nums) {
        if (nums.size() == 1)
            return 0;

        // cheating: n log n
        sort(nums.begin(), nums.end());

        int result = 0;
        for (int i = 1; i < nums.size(); i++)
        {
            auto diff = nums[i] - nums[i - 1];
            if (result < diff)
                result = diff;
        }

        return result;
    }
};
