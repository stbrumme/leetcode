class Solution {
public:
    int largestRectangleArea(vector<int>& heights) {
        map<int, int> start;

        heights.push_back(0);

        int best = 0;
        for (int i = 0; i < heights.size(); i++)
        {
            auto h = heights[i];
            auto left = i;

            auto higher = start.upper_bound(h);
            for (auto reduce = higher; reduce != start.end(); reduce++)
            {
                int area = reduce->first * (i - reduce->second);
                best = max(best, area);
                left = min(left, reduce->second);
            }

            if (higher != start.end() && higher->first == h)
                higher++;
            start.erase(higher, start.end());

            if (start.count(h) == 0)
                start[h] = left;
        }

        return best;
    }
};
