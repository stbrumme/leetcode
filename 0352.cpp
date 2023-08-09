class SummaryRanges {
    set<int> all;

public:
    void addNum(int value) {
        all.insert(value);
    }

    vector<vector<int>> getIntervals() {
        vector<vector<int>> result;
        if (all.empty())
            return result;

        int from = -2;
        int to   = -2;
        for (auto x : all)
        {
            if (x != to + 1)
            {
                // new interval
                if (from >= 0)
                    result.push_back({ from, to });
                from = to = x;
                continue;
            }

            to = x;
        }

        result.push_back({ from, to });
        return result;
    }
};
