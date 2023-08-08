class Solution {
public:
    bool canJump(vector<int>& nums) {
        if (nums.size() == 1)
            return true;

        vector<char> reach(nums.size() + 1, false);
        reach[0] = true;

        for (auto i = 0; i < nums.size(); i++)
        {
            if (!reach[i])
                continue;

            for (auto j = 1; j <= nums[i]; j++)
            {
                if (i + j == nums.size() - 1)
                    return true;
                if (i + j <  nums.size() - 1)
                    reach[i + j] = true;
            }
        }

        return false;
    }
};
