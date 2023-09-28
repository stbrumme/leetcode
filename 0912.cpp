class Solution {
public:
    vector<int> sortArray(vector<int>& nums)
    {
        if (nums.size() <= 1)
            return nums;

        // Python's just too slow ... had to switch to C++
        // in-place Radix-Sort
        map<int, int> radix; // slightly cheating: maps are sorted by default
        for (auto n : nums)
            radix[n]++;
        size_t pos = 0;
        for (auto r : radix)
            for (int i = 0; i < r.second; i++)
                nums[pos++] = r.first;

        return nums;
    }
};
