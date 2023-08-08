class Solution {
    int single, week, month;
    vector<int> travel;

    unordered_map<int, int> cache;

    int dp(int from, int paid)
    {
        if (cache.count(from) > 0)
            return cache[from] + paid;

        auto i = lower_bound(travel.begin(), travel.end(), from);
        if (i == travel.end())
            return paid;

        auto next = *i;

        auto s = dp(next +  1, paid + single);
        auto w = dp(next +  7, paid + week);
        auto m = dp(next + 30, paid + month);

        auto result = min(min(s,w),m);

        cache[from] = result - paid;
        return result;
    }

public:
    int mincostTickets(vector<int>& days, vector<int>& costs) {
        single = costs[0];
        week   = costs[1];
        month  = costs[2];

        travel = days;
        sort(travel.begin(), travel.end());

        cache.clear();

        return dp(0, 0);
    }
};
