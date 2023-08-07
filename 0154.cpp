class Solution {
public:
    int findMin(vector<int>& nums) {
        // brute-force
        return *min_element(nums.begin(), nums.end());
    }
};
