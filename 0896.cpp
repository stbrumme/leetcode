class Solution {
public:
    bool isMonotonic(vector<int>& nums) {
        int sign = 1;
        if (nums.back() - nums.front() < 0)
            sign = -1;

        for (size_t i = 1; i < nums.size(); i++)
            if ((nums[i] - nums[i - 1]) * sign < 0)
                return false;

        return true;
    }
};
