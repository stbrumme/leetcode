class Solution {
public:
    short increment(short x)
    {
        // find bit=0, clear all bits along the way
        int mask = 1;
        // overflow is okay and intended
        while (x & mask)
        {
            x ^= mask;
            mask <<= 1;
        }

        return x | mask;
    }

    int getSum(int a, int b)
    {
        if (a > b)
            swap(a, b);

        // short => 16 bits
        short aa = a;
        short bb = b;
        // a+b = 2*a + (b - a)
        int result = aa << 1;

        // slowly increment aa by 1 until bb - aa == 0
        while (aa < bb)
        {
            aa     = increment(aa);
            result = increment(result);
        }

        return result;
    }
};
