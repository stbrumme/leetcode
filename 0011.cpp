class Solution {
public:
    int maxArea(vector<int>& height) {
        map<int, int> last;
        for (int i = 0; i < height.size(); i++)
            last[height[i]] = i;

        auto maxx = 0;
        vector<int> prune;
        for (int i = 0; i < height.size(); i++)
        {
            int left = height.size() - i;
            int minHeight = maxx / left;

            prune.clear();
            auto l = last.lower_bound(minHeight);
            for (; l != last.end(); l++)
            {
                auto h = l->first;
                auto w = l->second - i;
                if (w <= 0)
                {
                    prune.push_back(h);
                    continue;
                }

                auto area = min(h, height[i]) * w;

                if (maxx < area)
                    maxx = area;
            }

            // prune
            for (auto h : prune)
                last.erase(h);
        }

        return maxx;
    }
};
