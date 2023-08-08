class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int64_t all = 1;
        int zeros = 0;
        for (auto n : nums)
            if (n == 0)
                zeros++;
            else
                all *= n;

        int allOneZero = all;
        if (zeros > 1)
            allOneZero = 0;
        if (zeros >= 1)
            all = 0;

        vector<int> result;
        for (auto n : nums)
        {
            if (n == 0)
                result.push_back(allOneZero);
            else
                result.push_back(all / n);
        }

        return result;
    }
};
