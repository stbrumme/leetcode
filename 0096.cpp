class Solution {
public:
    int numTrees(int n) {
        // problem 95 identified this as Catalan numbers
        // https://www.wolframalpha.com/input?i=1%2C2%2C5%2C14%2C42%2C132%2C429
        vector<int64_t> result =
        {
            1, 2, 5, 14, 42, 132, 429, 1430, 4862, 16796, 58786, 208012, 742900, 2674440, 9694845, 35357670, 129644790, 477638700, 1767263190, 6564120420, 24466267020, 91482563640, 343059613650, 1289904147324, 4861946401452, 18367353072152, 69533550916004, 263747951750360 };

        return result[n - 1];

    }
}
