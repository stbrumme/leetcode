class Solution {
public:
    int jump(vector<int>& nums) {
        if (nums.size() == 1)
            return 0;

        vector<int> steps(nums.size() + 1, 999999);
        steps[0] = 0;

        for (auto i = 0; i < nums.size(); i++)
        {
            if (steps[i] == 999999)
                continue;

            for (auto j = 1; j <= nums[i]; j++)
            {
                if (i + j >= steps.size())
                    break;

                if (steps[i + j] > steps[i] + 1)
                    steps[i + j] = steps[i] + 1;
            }
        }

        return steps[nums.size()  - 1];
    }
};
