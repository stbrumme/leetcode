class Solution {
public:
    vector<vector<int>> combine(int n, int k) {
        // n-k zeros and k ones
        vector<int> p(n-k, 0);
        for (int i = 0; i < k; i++)
            p.push_back(1);

        vector<vector<int>> result;
        result.reserve(10000);

        vector<int> add;
        do
        {
            add.clear();

            for (int i = 0; i < p.size(); i++)
                if (p[i] == 1)
                    add.push_back(i+1);

            result.push_back(add);
        } while (next_permutation(p.begin(), p.end()));

        return result;
    }
};
