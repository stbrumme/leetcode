class Solution {
public:
    int arrangeCoins(int n) {
        int64_t step = 0;
        int64_t available = 0;

        while (available < n)
        {
            step++;
            available += step;
        }

        if (n < available)
            step--;

        return step;
    }
};
