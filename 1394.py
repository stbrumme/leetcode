class Solution:
    def findLucky(self, arr: List[int]) -> int:
        freq = defaultdict(int)
        for a in arr:
            freq[a] += 1

        for f in sorted(freq, reverse = True):
            if f == freq[f]:
                return f

        return -1
