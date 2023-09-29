class Solution {
public:
    vector<int> fallingSquares(vector<vector<int>>& positions) {
        map<int, int> height;
        height[0] = 0; // ground plane
        int highest = 0;

        vector<int> result;
        for (auto p : positions)
        {
            auto x1 = p[0];
            auto x2 = x1 + p[1];
            auto y  = p[1];

            // directly below
            auto l = height.upper_bound(x1);
            auto r = height.lower_bound(x2);

            // highest square
            auto peak = prev(l)->second;
            auto last = peak;
            for (auto scan = l; scan != r; scan++)
            {
                peak = max(peak, scan->second);
                last = scan->second;
            }
            // overwrite them
            if (l != r)
                height.erase(l, r);
            height[x1] = peak + y; // left up
            if (height.count(x2) == 0) // right down
                height[x2] = last;

            highest = max(highest, peak + y);
            result.push_back(highest);
        }

        return result;
    }
};
