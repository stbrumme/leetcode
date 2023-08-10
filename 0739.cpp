class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {
        reverse(temperatures.begin(), temperatures.end());

        vector<int> result;
        result.reserve(temperatures.size());

        const int maxtemp = 100;
        const int invalid = -1;
        vector<int> last(maxtemp + 1, invalid);
        for (int i = 0; i < temperatures.size(); i++)
        {
            auto current = temperatures[i];

            // optimize
            const int scan = 10;
            if (i > scan)
            {
                bool fast = false;
                for (int j = 1; j < scan; j++)
                    if (temperatures[i - j] > current)
                    {
                        fast = true;
                        result.push_back(j);
                        break;
                    }

                if (fast)
                {
                    last[current] = i;
                    continue;
                }
            }

            int best = invalid;
            for (int j = current + 1; j < last.size(); j++)
                if (best < last[j] && last[j] != invalid)
                {
                    best = last[j];
                    if (best == i - 1)
                        break;
                }

            if (best == invalid)
                result.push_back(0);
            else
                result.push_back(i - best);

            last[current] = i;
        }

        reverse(result.begin(), result.end());
        return result;
    }
};
