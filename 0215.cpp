class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {
        auto n = nums.size() - k;
        nth_element(nums.begin(), nums.begin() + n, nums.end());
        return nums[n];
    }
};
