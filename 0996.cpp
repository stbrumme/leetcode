class Solution {
public:
    int numSquarefulPerms(vector<int>& nums) {
        sort(nums.begin(), nums.end());

        vector<int> squares;
        for (int i = 0; i*i < 1000000000; i++)
            squares.push_back(i*i);

        int result = 0;
        do
        {
            bool ok = true;
            for (int i = 1; i < nums.size(); i++)
            {
                auto sum = nums[i - 1] + nums[i];
                if ((nums[i] > 2 && nums[i - 1] == nums[i]) || // performance trick: a+a is never a square if a > 2
                    !binary_search(squares.begin(), squares.end(), sum))
                {
                    ok = false;

                    // skip permutations
                    sort   (nums.begin() + i + 1, nums.end());
                    reverse(nums.begin() + i + 1, nums.end());

                    break;
                }
            }

            if (ok)
                result++;
        } while(next_permutation(nums.begin(), nums.end()));

        return result;
    }
};
