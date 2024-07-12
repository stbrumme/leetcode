class CountIntervals {
    std::map<int, int> covered; // left => right
    int numbers;

public:
    CountIntervals()
    : numbers(0)
    {}

    void add(int left, int right)
    {
        // merge overlaps with other intervals
        while (true)
        {
            auto merge  = covered.lower_bound(left);
            auto follow = covered.upper_bound(right);

            // potentially no overlap, still need to check predecessor
            if (merge == follow)
            {
                // there's none
                if (merge == covered.begin())
                    break;

                merge = prev(merge);
                if (merge->second < left)
                    break;
            }

            // subtract all integers of that interval
            numbers -= merge->second - merge->first + 1;

            // merge left
            if (left  > merge->first)
                left  = merge->first;

            // merge right
            if (right < merge->second)
                right = merge->second;

            covered.erase(merge);
        }

        // add (merged) interval
        covered.insert({ left, right });
        numbers += right - left + 1;
    }

    int count() const
    {
        return numbers;
    }
};
