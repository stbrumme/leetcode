class Solution {
public:
    string toLowerCase(string s) {
        for (auto& c : s)
            if (c >= 'A' && c <= 'Z')
                c += 'a' - 'A';

        return s;
    }
};
