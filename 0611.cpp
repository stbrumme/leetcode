class Solution {
public:
    int triangleNumber(vector<int>& nums) {
        sort(nums.begin(), nums.end());

        int result = 0;
        for (int i = 0; i < nums.size(); i++)
        {
            if (nums[i] == 0)
                continue;

            for (int j = i + 1; j < nums.size(); j++)
            {
                auto minLength = nums[i] + nums[j];
                auto third = lower_bound(nums.begin(), nums.end(), minLength);
                auto toobig = distance(third, nums.end());
                result += nums.size() - toobig - j - 1;
            }
        }

        return result;
    }
};
