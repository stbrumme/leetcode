class Solution {
public:
    bool isSubsequence(string s, string t) {
        if (s.size() > t.size())
            return false;

        if (s.empty())
            return true;

        int S = 0;
        for (int T = 0; T < t.size(); T++)
            if (s[S] == t[T])
                S++;

        return S == s.size();
    }
};
