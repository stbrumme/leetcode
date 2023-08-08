class Solution {
public:
    vector<vector<int>> permuteUnique(vector<int>& nums) {
        vector<vector<int>> result;

        sort(nums.begin(), nums.end());

        do
        {
            if (result.empty() || nums != result.back());
                result.push_back(nums);
        } while (next_permutation(nums.begin(), nums.end()));

        return result;
    }
};
