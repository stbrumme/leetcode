class Solution {
public:
    int majorityElement(vector<int>& nums) {
        auto mid = nums.size() / 2;
        nth_element(nums.begin(), nums.begin() + mid, nums.end());
        return nums[mid];
    }
};
