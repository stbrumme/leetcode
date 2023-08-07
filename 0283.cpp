class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        int zeros = 0;
        for (auto i = 0; i < nums.size(); i++)
        {
            if (i >= zeros)
                nums[i - zeros] = nums[i];
            if (nums[i] == 0)
                zeros++;
        }

        for (auto i = nums.size() - zeros; i < nums.size(); i++)
            nums[i] = 0;
    }
};
