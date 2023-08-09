class Solution {
public:
    bool containsNearbyDuplicate(vector<int>& nums, int k) {
        unordered_map<int, int> last;

        for (int i = 0; i < nums.size(); i++)
        {
            auto current = nums[i];
            if (last.count(current) > 0)
                if (i - last[current] <= k)
                    return true;

            last[current] = i;
        }

        return false;
    }
};
