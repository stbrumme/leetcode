class Solution {
public:
    int minCostClimbingStairs(vector<int>& cost) {
        int total[1002] = { 0 };

        total[2] = cost[0] < cost[1] ? cost[0] : cost[1];

        for (int i = 0; i < cost.size(); i++)
        {
            int paid = total[i] + cost[i];

            if (total[i+1] > paid)
                total[i+1] = paid;

            total[i+2] = paid;
        }

        return total[cost.size()];
    }
};
