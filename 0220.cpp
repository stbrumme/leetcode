class Solution {
public:
    bool containsNearbyAlmostDuplicate(vector<int>& nums, int indexDiff, int valueDiff) {
        // see 219
        map<int, int> last;

        // faster for test cases ...
        reverse(nums.begin(), nums.end());

        for (int i = 0; i < nums.size(); i++)
        {
            auto current = nums[i];
            auto mid = last.lower_bound(current);

            auto check = mid;
            // scan right
            while (check != last.end())
            {
                if (abs(check->first - current) > valueDiff)
                    break;

                if (abs(check->second - i)      <= indexDiff)
                    return true;

                check++;
            }

            // scan left
            check = mid;
            while (check != last.begin())
            {
                check--;

                if (abs(check->first - current) > valueDiff)
                    break;

                if (abs(check->second - i)      <= indexDiff)
                    return true;
            }

            // add
            last[current] = i;
        }

        return false;
    }
};
