class Solution {
public:
    int getMinSwaps(string num, int k)
    {
        int result = 0;

        // C++ next_permutation is so much better than Python's permutation() ...
        auto wonderful = num;
        while (k--)
            std::next_permutation(wonderful.begin(), wonderful.end());
        // that's all we need to find the k-th wonderful number !

        // look for mismatches
        for (size_t same = 0; same < num.size(); same++)
            if (num[same] != wonderful[same])
            {
                // find next position of wonderful[same] in nums[]
                auto scan = num.find(wonderful[same], same + 1);

                // swap digit to correct position: left-rotate by one
                std::rotate(num.begin() + same, num.begin() + scan, num.begin() + scan + 1);
                result += scan - same;
            }

        return result;
    }
};
