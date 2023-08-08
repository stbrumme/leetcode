class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        auto i = unique(nums.begin(), nums.end());
        return distance(nums.begin(), i);
    }
};
