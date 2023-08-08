class Solution {
public:
    vector<string> generateParenthesis(int n) {
        string s;
        for (int i = 0; i < n; i++)
            s += "(";
        for (int i = 0; i < n; i++)
            s += ")";

        vector<string> result;

        do
        {
            // first must be (
            if (s[0] != '(')
                break;

            bool ok = true;
            int depth = 0;
            for (auto c : s)
            {
                if (c == '(')
                    depth++;
                else
                    depth--;

                if (depth < 0)
                {
                    ok = false;
                    break;
                }
            }
            if (ok)
                result.push_back(s);
        } while (next_permutation(s.begin(), s.end()));

        return result;
    }
};

