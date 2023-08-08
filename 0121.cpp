class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int high = prices[0];
        int low  = prices[0];

        int best = 0;

        for (auto p : prices)
        {
            if (low > p)
            {
                low = p;
                high = p;
            }
            if (high < p)
                high = p;

            if (best < high - low)
                best = high - low;
        }

        return best;
    }
};
