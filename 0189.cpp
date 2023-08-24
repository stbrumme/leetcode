class Solution {
public:
    void rotate(vector<int>& nums, int k) {
        k %= nums.size();
        k = nums.size() - k;
        std::rotate(nums.begin(), nums.begin() + k, nums.end());
    }
};
