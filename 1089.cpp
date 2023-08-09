class Solution {
public:
    void duplicateZeros(vector<int>& arr) {
        vector<int> two;
        for (auto x : arr)
        {
            two.push_back(x);
            if (x == 0)
                two.push_back(0);

            if (two.size() > arr.size())
                break;
        }

        two.resize(arr.size());
        arr = move(two);
    }
};
