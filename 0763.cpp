class Solution {
public:
    vector<int> partitionLabels(string s) {
        unordered_map<char, int> freq;
        for (auto c : s)
            freq[c]++;

        vector<int> result;

        int pos = 0;
        unordered_map<char, int> need;
        while (pos < s.size())
        {
            need.clear();
            char current = s[pos++];

            if (freq[current] == 1)
            {
                result.push_back(1);
                continue;
            }
            need[current] = freq[current] - 1;

            auto length = 1;
            while (!need.empty())
            {
                auto next = s[pos++];
                length++;
                if (need.count(next) == 0)
                {
                    if (freq[next] > 1)
                        need[next] = freq[next] - 1;
                }
                else
                {
                    need[next]--;
                    if (need[next] == 0)
                        need.erase(next);
                }
            }
            result.push_back(length);
        }

        return result;
    }
};
