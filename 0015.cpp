class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        vector<vector<int>> result;

        map<int, int> freq;
        for (auto n : nums)
            freq[n]++;

        // at most 3x each number
        nums.clear();
        for (auto f : freq)
            for (auto i = 0; i < f.second && i <= 3; i++)
                nums.push_back(f.first);

        for (int i = 0; i < nums.size(); i++)
            for (int j = i+1; j < nums.size(); j++)
            {
                int need = -(nums[i] + nums[j]);

                auto minK = j + 1;
                auto pos = lower_bound(nums.begin() + minK, nums.end(), need);
                if (pos != nums.end() && *pos == need)
                    result.push_back({ nums[i], nums[j], need });
            }

        sort(result.begin(), result.end());
        auto last = unique(result.begin(), result.end());
        result.erase(last, result.end());
        return result;
    }
};
