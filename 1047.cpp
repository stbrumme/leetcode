class Solution {
public:
    string removeDuplicates(string s) {
        if (s.size() <= 1)
            return s;

        list<char> seq(s.begin(), s.end());

        auto i = seq.begin();
        while (next(i) != seq.end())
        {
            if (*i == *next(i))
            {
                i = seq.erase(i, next(next(i)));
                if (i != seq.begin())
                    i--;
            }
            else
                i++;
        }

        return { seq.begin(), seq.end() };
    }
};
