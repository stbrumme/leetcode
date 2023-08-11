class Solution {
    struct point
    {
        int x, y;
    };

    int dot(const point& a, const point& b, const point& c)
    {
        return (b.y - a.y) * (c.x - b.x) -
               (b.x - a.x) * (c.y - b.y);
    }

public:
    vector<vector<int>> outerTrees(vector<vector<int>>& trees) {
        // convex hull / Gift Wrapping by Jarvis
        if (trees.size() < 3)
            return { trees };

        vector<point> all;
        for (auto t : trees)
            all.push_back({ t[0], t[1] });

        // first tree
        int leftmost = 0;
        for (int i = 1; i < all.size(); i++)
            if (all[leftmost].x >= all[i].x) // "equal" => including colinear
                leftmost = i;

        // minimal hull
        vector<int> hull;
        int current = leftmost;
        do
        {
            hull.push_back(current);

            int next = current + 1;
            next %= trees.size();

            for (int i = 0; i < trees.size(); i++)
                if (dot(all[current], all[i], all[next]) < 0)
                    next = i;

            current = next;
        } while (current != leftmost);

        // touching the fence (=> not minimal convex hull)
        auto hsize = hull.size();
        for (int j = 0; j < hsize; j++)
        {
            for (int i = 0; i < all.size(); i++)
            {
                auto prev = j - 1;
                if (j == 0)
                    prev = hsize - 1;

                if (dot(all[hull[prev]], all[i], all[hull[j]]) == 0)
                    hull.push_back(i);
            }
        }

        // no duplicates
        sort(hull.begin(), hull.end());
        auto last = unique(hull.begin(), hull.end());
        hull.erase(last, hull.end());

        vector<vector<int>> result;
        for (auto h : hull)
            result.push_back({ all[h].x, all[h].y });
        return result;
    }
};
