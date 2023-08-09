class Solution {
public:
    string getPermutation(int n, int k) {
        // brute-force
        string s;
        for (int i = 1; i <= n; i++)
            s += i + '0';

        for (; k > 1; k--)
            next_permutation(s.begin(), s.end());

        return s;
    }
};
