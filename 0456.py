class Solution {
public:
    bool find132pattern(vector<int>& nums) {
        if (nums.size() < 3)
            return false;

        map<int, int> lowHigh;
        auto low  = nums[0];
        auto high = max(nums[1], nums[2]);
        lowHigh[nums[0]] = high;
        lowHigh[nums[1]] = high;

        for (int i = 2; i < nums.size(); i++)
        {
            auto current = nums[i];
            if (nums[i] == nums[i - 1]) // optimization
                continue;

            if (current > low && current < high)
                return true;

            // update intervals
            auto scan = lowHigh.lower_bound(current);
            if (scan != lowHigh.begin())
                do
                {
                    scan--;
                    if (scan->second > current)
                        return true;
                } while (scan != lowHigh.begin());

            if (current == low || current == high)
                continue;

            if (current > high)
            {
                high = current;
                vector<int> same;
                // move highs higher
                for (auto& update : lowHigh)
                    if (update.second < high)
                    {
                        update.second = high;
                        same.push_back(update.first);
                    }

                // erase redundant entries
                for (int i = 1; i < same.size(); i++)
                    lowHigh.erase(same[i]);

                continue;
            }

            // current < low
            low = high = current;
            lowHigh[current] = current;
        }

        return false;
    }
};
