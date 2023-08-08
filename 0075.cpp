class Solution {
public:
    void sortColors(vector<int>& nums) {
        vector<int> freq(3, 0);
        for (auto n : nums)
            freq[n]++;

        nums.clear();

        nums.insert(nums.end(), freq[0], 0);
        nums.insert(nums.end(), freq[1], 1);
        nums.insert(nums.end(), freq[2], 2);
    }
};
