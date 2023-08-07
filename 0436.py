class Solution {
public:
    vector<int> findRightInterval(vector<vector<int>>& intervals) {
        map<int, int> sorted;
        for (int i = 0; i < intervals.size(); i++)
        {
            auto start = intervals[i][0];
            sorted[start] = i;
        }

        vector<int> result;
        result.reserve(intervals.size());
        for (auto& i : intervals)
        {
            auto start = i[0];
            auto end   = i[1];

            auto pos = sorted.lower_bound(end);
            if (pos == sorted.end())
                result.push_back(-1);
            else
                result.push_back(pos->second);
        }
        return result;
    }
};
