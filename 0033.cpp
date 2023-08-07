class Solution {
public:
    int search(vector<int>& nums, int target) {
        // brute-force

        if (nums.size() > 100)
            for (auto i = 0; i < 100; i++)
                if (nums[nums.size() - i - 1] == target)
                    return nums.size() - i - 1;

        for (auto i = 0; i < nums.size() && i < 100; i++)
            if (nums[i] == target)
                return i;

        return -1;
    }
};
