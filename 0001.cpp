class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        auto sorted = nums;
        sort(sorted.begin(), sorted.end());

        for (int i = 0; i < nums.size(); i++)
        {
            auto need = target - nums[i];
            if (!binary_search(sorted.begin(), sorted.end(), need))
                continue;

            for (int j = i+1; j < nums.size(); j++)
            {
                if (nums[i] + nums[j] == target)
                    return { i,j };
            }
        }

        return {};
    }
};
