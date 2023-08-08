class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        for (auto i = 0; i < nums.size(); i++)
            if (nums[i] == val)
                nums[i] = 999;

        sort(nums.begin(), nums.end());

        while (!nums.empty() && nums.back() == 999)
            nums.pop_back();

        return nums.size();
    }
};
