class Solution {
public:
    int hIndex(vector<int>& citations) {
        reverse(citations.begin(), citations.end());
        int h = 0;
        while (h < citations.size())
        {
            if (citations[h] <= h)
                break;
            h++;
        }

        return h;
    }
};
