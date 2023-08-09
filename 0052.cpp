class Solution {
public:
    int totalNQueens(int n) {
        // see problem 51, even simpler

        vector<int> order;
        for (int i = 0; i < n; i++)
            order.push_back(i);

        int result = 0;
        do
        {
            int blockLeft  = 0;
            int blockRight = 0;

            bool ok = true;

            int line;
            for (line = 0; line < order.size(); line++)
            {
                int pos = order[line];

                int mask = 1 << pos;
                ok &= (mask & blockLeft)  == 0;
                ok &= (mask & blockRight) == 0;

                blockLeft  <<= 1;
                blockRight >>= 1;

                blockRight &= (1 << n) - 1;

                if (!ok)
                    break;

                blockLeft  |= mask << 1;
                blockRight |= mask >> 1;
            }

            if (ok)
                result++;
            else
            {
                // skip permutations
                if (line < n - 1)
                {
                    // not perfect, but fast
                    sort   (order.begin() + line + 1, order.end());
                    reverse(order.begin() + line + 1, order.end());
                }
            }
        } while (next_permutation(order.begin(), order.end()));

        return result;
    }
};

