class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        lengths = defaultdict(int)
        for n in arr:
            lengths[n] = max(lengths[n], lengths[n - difference] + 1)

        return max(lengths.values())