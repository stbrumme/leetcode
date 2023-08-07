class Solution {
public:
    int minPathSum2(vector<vector<int>>& grid) {
        int w = grid.size();
        int h = grid[0].size();

        multimap<int, pair<int, int>> next;
        next.insert({ grid[0][0], { 0, 0 } });

        set<pair<int, int>> done;

        vector<vector<int>> cheapest;
        cheapest.resize(w);
        for (auto& c : cheapest)
            c.resize(h);

        int iteration = 1;
        while (true)
        {
            auto n = next.begin();
            auto cost = n->first;
            auto x = n->second.first;
            auto y = n->second.second;

            cheapest[x][y] = cost;

            if (x == w-1 && y == h-1)
                return cost;

            next.erase(next.begin());
            if (done.count({ x, y }) > 0)
                continue;
            done.insert({ x, y });

            if (x < w-1)
                next.insert({ cost + grid[x+1][y], { x+1, y } });
            if (y < h-1)
                next.insert({ cost + grid[x][y+1], { x, y+1 } });
        }

        return 0;
    }


    int minPathSum(vector<vector<int>>& grid) {
        int h = grid.size();
        int w = grid[0].size();

        vector<vector<int>> cheapest;
        cheapest.resize(h);
        for (auto& c : cheapest)
            c.resize(w);

        cheapest[0][0] = grid[0][0];

        for (int x = 0; x < w; x++)
            for (int y = 0; y < h; y++)
            {
                int lowest = 9999999;
                if (x > 0)
                    lowest          = grid[y][x] + cheapest[y][x-1];
                if (y > 0 && lowest > grid[y][x] + cheapest[y-1][x])
                    lowest          = grid[y][x] + cheapest[y-1][x];

                if (x > 0 || y > 0)
                    cheapest[y][x] = lowest;
            }

        return cheapest[h-1][w-1];
    }
};
