class Solution {
public:
    bool isPerfectSquare(int num) {
        int64_t step = 1 << 16;
        int64_t guess = 0;

        while (step > 0)
        {
            while ((guess + step) * (guess + step) <= num)
                guess += step;

            step >>= 1;
        }

        return guess * guess == num;
    }
};
