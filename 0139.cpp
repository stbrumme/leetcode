class Solution {
    unordered_set<string> dict;
    unordered_map<int, bool> cache;

    bool dp(string& s, int index)
    {
        if (index == s.size())
            return true;

        if (cache.count(index) > 0)
            return cache[index];

        string word;
        for (int i = index; i < s.size(); i++)
        {
            word += s[i];
            if (dict.count(word) > 0)
                if (dp(s, i + 1))
                {
                    cache[index] = true;
                    return true;
                }
        }

        cache[index] = false;
        return false;
    }

public:
    bool wordBreak(string s, vector<string>& wordDict) {
        cache.clear();
        dict.clear();
        for (auto w : wordDict)
            dict.insert(w);

        return dp(s, 0);
    }
};

