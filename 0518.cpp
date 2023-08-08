class Solution {
public:
    int change(int amount, vector<int>& coins) {
        vector<int> ways, next;
        ways.resize(amount + 1, 0);
        ways[0] = 1;

        for (auto c : coins)
        {
            next = ways;
            for (int base = 0; base < amount; base++)
            {
                if (ways[base] == 0)
                    continue;

                for (int sum = base + c; sum <= amount; sum += c)
                    next[sum] += ways[base];
            }
            swap(ways, next);
        }

        return ways[amount];
    }
};
