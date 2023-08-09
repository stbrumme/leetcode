class Solution {
    unordered_set<string> dict;
    vector<string> result;

    void dp(string s, string previous)
    {
        if (s.empty())
        {
            if (previous.empty())
                return;

            if (previous.back() == ' ')
                previous.erase(previous.end() - 1);
            result.push_back(previous);
            return;
        }

        string word;
        while (!s.empty())
        {
            word += s[0];
            s.erase(0, 1);

            if (dict.count(word) == 0)
                continue;

            dp(s, previous + word + ' ');
        }
    }

public:
    vector<string> wordBreak(string s, vector<string>& wordDict) {
        dict.clear();
        for (auto w : wordDict)
            dict.insert(w);
        result.clear();

        dp(s, "");

        return result;
    }
};
