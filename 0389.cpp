class Solution {
public:
    char findTheDifference(string s, string t) {
        unordered_map<char, int> freq;
        for (auto c : s)
            freq[c]++;
        for (auto c : t)
            freq[c]--;

        for (auto f : freq)
            if (f.second != 0)
                return f.first;
        return 0;
    }
};
