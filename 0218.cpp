class Solution {
public:
    vector<vector<int>> getSkyline(vector<vector<int>>& buildings) {
        vector<vector<int>> result;

        multimap<int, int> changes; // y => last x
        set<int> walls;
        for (const auto& b : buildings)
        {
            changes.insert(make_pair(b[0], +b[2])); // start
            changes.insert(make_pair(b[1], -b[2])); // end
            walls.insert(b[0]);
            walls.insert(b[1]);
        }

        map<int, int> y;
        y[0] = 1; // ground
        int last = 0;

        // merge
        for (auto x : walls)
        {
            auto same = changes.equal_range(x);
            for (auto i = same.first; i != same.second; i++)
            {
                auto height = i->second;
                if (height > 0)
                    y[height]++;
                else
                {
                    auto posHeight = -height;
                    y[posHeight]--;
                    if (y[posHeight] == 0)
                        y.erase(posHeight);
                }
            }

            int high = y.rbegin()->first;
            if (last == high)
                continue;

            result.push_back({ x, high });
            last = high;
        }

        return result;
    }
};
