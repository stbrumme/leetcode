class Solution {
public:
    bool isRobotBounded(string instructions) {
        // 4x
        instructions += instructions;
        instructions += instructions;

        int x = 0;
        int y = 0;
        int dx = 0;
        int dy = +1;

        for (auto i : instructions)
        {
            if (i == 'G')
            {
                x += dx;
                y += dy;
                continue;
            }

            // assume 'L'
            if      (dx == +1) { dx = 0; dy = +1; }
            else if (dx == -1) { dx = 0; dy = -1; }
            else if (dy == +1) { dx = -1; dy = 0; }
            else               { dx = +1; dy = 0; }

            // flip
            if (i == 'R')
            {
                dx = -dx;
                dy = -dy;
            }
        }

        return x == 0 && y == 0; // && dx == 0 && dy == +1;
    }
};

