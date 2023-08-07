class Solution {
    static vector<int> minn;

    void precompute()
    {
        const int limit = 10000;
        const int invalid = 9999999;

        minn.resize(limit+1, invalid);

        int iteration = 1;
        for (auto i = 1; i*i <= limit; i++)
            minn[i*i] = 1;

        int numFound = 9999999;
        while (numFound > 0)
        {
            numFound = 0;
            iteration++;

            for (auto i = limit; i >= 1; i--)
                if (minn[i] != invalid)
                    for (auto j = 1; i + j*j <= limit; j++)
                        if (minn[i + j*j] == invalid)
                        {
                            minn[i + j*j] = iteration;
                            numFound++;
                        }
        }
    }

public:
    int numSquares(int n) {
        if (minn.empty())
            precompute();

        return minn.at(n);
    }
};

vector<int> Solution::minn;
