class Solution {
public:
    int firstBadVersion(int n) {
        int64_t N = int64_t(n) + 1; // one-based

        int64_t step  = 1;
        while (step*2 < N)
            step *= 2;

        int64_t guess = N / 2;
        while (true)
        {
            step >>= 1;

            bool isBad = isBadVersion(guess-1); // zero-based
            if (isBad)
                guess -= step;
            else
                guess += step;

            if (step == 0)
            {
                if (isBad)
                    return guess-1;
                else
                    return guess;
            }
        }

        return guess;
    }
};
