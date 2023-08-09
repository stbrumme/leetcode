class Solution {
public:
    bool wordPattern(string pattern, string s) {
        map<char, string> p;

        stringstream text;
        text.str(s);

        for (auto c : pattern)
        {
            string word;
            text >> word;

            if (word.empty())
                return false;

            if (p.count(c) == 0)
            {
                p[c] = word;
                continue;
            }

            if (word != p[c])
                return false;
        }

        // make sure patterns are unique
        unordered_set<string> u;
        for (auto i : p)
        {
            if (u.count(i.second) > 0)
                return false;
            u.insert(i.second);
        }

        string x;
        text >> x;
        return x.empty();
    }
};
