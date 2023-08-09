class Solution {
public:
    int findMaximizedCapital(int k, int w, vector<int>& profits, vector<int>& capital) {
        map<int, vector<short>> proj; // mincapital => profit
        for (int i = 0; i < profits.size(); i++)
            proj[capital[i]].push_back(profits[i]);

        int result = w;

        vector<short> avail;
        auto last = proj.upper_bound(result);
        for (auto i = proj.begin(); i != last; i++)
            avail.insert(avail.end(), i->second.begin(), i->second.end());
        sort(avail.begin(), avail.end());

        for (int i = 0; i < k; i++)
        {
            if (avail.empty())
                break;

            auto pick = avail.back();
            avail.pop_back();

            auto prev = result;
            result += pick;

            auto from = last;
            last = proj.upper_bound(result);
            if (from != last)
            {
                for (auto j = from; j != last; j++)
                {
                    avail.insert(avail.end(), j->second.begin(), j->second.end());
                    j->second.clear();
                    j->second.shrink_to_fit();
                }
                sort(avail.begin(), avail.end());
            }
        }

        return result;
    }
};
