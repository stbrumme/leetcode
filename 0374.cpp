class Solution {
public:
    int guessNumber(int n) {
        int64_t pick = 1 << 30; // halfway between 1 and 2^31 - 1
        int64_t step = pick >> 1;

        while (true)
        {
            auto hint = guess(pick);
            if (hint == 0)
                break;

            pick += step * hint;
            step >>= 1;
        }

        return pick;
    }
};
