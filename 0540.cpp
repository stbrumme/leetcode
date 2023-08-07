class Solution {
public:
    int singleNonDuplicate(vector<int>& nums) {
        // XOR trick
        int result = 0;
        for (auto x : nums)
            result ^= x;

        return result;
    }
};
