class Solution {
public:
    string addBinary(string a, string b) {
        reverse(a.begin(), a.end());
        reverse(b.begin(), b.end());

        while (a.size() < b.size())
            a += '0';
        while (b.size() < a.size())
            b += '0';

        string result;
        result.reserve(a.size() + 1);

        int carry = 0;
        for (int i = 0; i < a.size(); i++)
        {
            int sum = carry + (a[i] - '0') + (b[i] - '0');

            result += '0' + (sum & 1);
            carry = sum >> 1;
        }

        if (carry > 0)
            result += '1';

        reverse(result.begin(), result.end());

        return result;
    }
};
