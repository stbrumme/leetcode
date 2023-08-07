class Solution {
public:
    bool checkStraightLine(vector<vector<int>>& coordinates) {
        // straight
        int x1 = coordinates[0][0];
        int y1 = coordinates[0][1];
        bool xonly = true;
        bool yonly = true;
        for (auto c : coordinates)
        {
            if (c[0] != x1)
                xonly = false;
            if (c[1] != y1)
                yonly = false;

            if (!xonly && !yonly)
                break;
        }

        if (xonly || yonly)
            return true;

        int dx = coordinates[0][0] - coordinates[1][0];
        int dy = coordinates[0][1] - coordinates[1][1];

        double epsilon = 1e-15;
        double r = double(dx) / dy;

        for (int i = 2; i < coordinates.size(); i++)
        {
            dx = coordinates[i][0] - coordinates[0][0];
            dy = coordinates[i][1] - coordinates[0][1];
            double r2 = double(dx) / dy;

            if (fabs(r2 - r) > 1000*epsilon)
                return false;
        }

        return true;
    }
};
