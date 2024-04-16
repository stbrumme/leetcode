class Solution {
public:
    int minAbsoluteDifference(vector<int>& nums, int x)
    {
        // each number minus itself is zero
        if (x == 0)
            return 0;

        int result = 999999999;

        // iterator pointing to current element
        auto i = nums.begin() + x;

        // all elements seen at least x steps ago
        std::set<int> old;

        for (; i != nums.end(); i++)
        {
            // one element "gets old" and becomes relevant for the difference check
            old.insert(*(i - x));

            // find old element being larger or equal
            auto value = *i;
            auto next = old.lower_bound(value);

            if (next != old.end())
            {
                // perfect match
                if (*next == value)
                    return 0;
                result = std::min(result, *next - value);
            }

            // old element being smaller
            if (next != old.begin())
                result = std::min(result, value - *std::prev(next));
        }

        return result;
    }
};
