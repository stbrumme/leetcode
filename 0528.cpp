class Solution {
    vector<int64_t> sum;
public:
    Solution(vector<int>& w) {
        sum.reserve(w.size());

        int64_t total = 0;
        for (auto x : w)
        {
            total += x;
            sum.push_back(total);
        }
    }

    int pickIndex() {
        int maxx = sum.back();

        std::random_device r;
        std::default_random_engine engine(r());
        std::uniform_int_distribution<int> uniform_dist(1, maxx);
        int x = uniform_dist(engine);

        auto p = lower_bound(sum.begin(), sum.end(), x);
        return distance(sum.begin(), p);
    }
};
