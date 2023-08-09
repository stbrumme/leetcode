class Solution {
public:
    string reverseWords(string s) {
        stringstream text;
        text.str(s);

        string result, word;
        while (text >> word)
        {
            if (!result.empty())
                result = word + ' ' + result;
            else
                result = word;
        }

        return result;
    }
};
