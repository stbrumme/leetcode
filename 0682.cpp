class Solution {
public:
    int calPoints(vector<string>& operations) {
        vector<int> r;
        for (auto o : operations)
        {
            if (o == "C")
            {
                r.pop_back();
                continue;
            }
            if (o == "D")
            {
                r.push_back(2 * r.back());
                continue;
            }
            if (o == "+")
            {
                r.push_back(r[r.size() - 2] + r[r.size() - 1]);
                continue;
            }

            r.push_back(stoi(o));
        }

        int sum = 0;
        for (auto x : r)
            sum += x;

        return sum;
    }
};
