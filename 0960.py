class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        size = len(strs[0])

        # longest increasing subsequence (LIS) for all words
        good = [ 1 ] * size
        for end in range(1, size):
            for start in range(end):
                if all(word[start] <= word[end] for word in strs):
                    good[end] = max(good[end], good[start] + 1)

        # delete everything not part of the LIS
        return size - max(good)
