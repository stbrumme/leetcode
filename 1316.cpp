class Solution {
public:
    int distinctEchoSubstrings(string text) {
        unordered_set<string> found;

        for (int length = 1; length <= text.size() / 2; length++)
        {
            for (int pos = 0; pos + 2*length <= text.size(); pos++)
            {
                // optimization
                if (text[pos + length - 1] != text[pos + length + length - 1])
                    continue;

                bool ok = true;
                for (int i = pos; i < pos + length - 1; i++) // -1 => opt
                    if (text[i] != text[i + length])
                    {
                        ok = false;
                        break;
                    }

                if (ok)
                    found.insert(text.substr(pos, length));
            }
        }

        return found.size();
    }
};
