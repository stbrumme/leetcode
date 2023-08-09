class Solution {
public:
    int countTriplets(vector<int>& nums) {
        const int limit = 1 << 16;
        vector<short> two(limit, 0);

        for (int i = 0; i < nums.size(); i++)
            two[nums[i]]++; // a & a

        for (int i = 0; i < nums.size(); i++)
            for (int j = i+1; j < nums.size(); j++)
            {
                auto x = nums[i] & nums[j];
                two[x] += 2; // a & b = b & a
            }

        // brute-force
        int result = 0;
        for (int i = 0; i < nums.size(); i++)
            for (int mask = 0; mask < limit; mask++)
                if ((mask & nums[i]) == 0)
                    result += two[mask];

        return result;
    }
};
