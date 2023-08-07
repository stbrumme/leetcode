class Solution {
public:
    int mySqrt(int x) {
        int64_t step = 1 << 16;
        int guess = 0;

        while (step > 0)
        {
            if ((guess + step) * (guess + step) <= x)
                guess += step;
            step >>= 1;
        }

        return guess;
    }
};
