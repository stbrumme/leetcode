class Solution {
public:
    int arraySign(vector<int>& nums) {
        int result = 1;
        for (auto x : nums)
        {
            if (x == 0)
                return 0;
            if (x < 0)
                result = -result;
        }
        return result;
    }
};
