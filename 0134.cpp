class Solution {
public:
    int canCompleteCircuit(vector<int>& gas, vector<int>& cost) {
        int totalgas = 0;
        int totalcost = 0;
        for (auto x : gas)
            totalgas += x;
        for (auto x : cost)
            totalcost += x;
        if (totalgas < totalcost)
            return -1;

        int tank = 0;
        int start = 0;
        for (int i = 0; i < gas.size(); i++)
        {
            if (tank < 0)
            {
                start = i;
                tank = 0;
            }

            tank += gas[i];
            tank -= cost[i];
        }
        return start;
    }
};
