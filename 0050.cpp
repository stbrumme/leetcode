class Solution {
public:
    double myPow(double x, int n) {
        if (x == 0)
            return x;
        if (n == 0)
            return 1;

        int64_t N = n;

        if (N < 0)
        {
            x = 1 / x;
            N = -N;
        }

        double result = x;
        N--;

        while (N > 0)
        {
            if (N & 1)
            {
                result *= x;
                N--;
            }
            else
            {
                x *= x;
                N >>= 1;
            }
        }
        return result;
    }
};
