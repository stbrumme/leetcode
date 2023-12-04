class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        freq = defaultdict(int)
        for a in arr:
            freq[a] += 1

        keys = sorted(freq, key = lambda x : abs(x))
        for k in keys:
            # map each number
            freq[2 * k] -= freq[k]
            if freq[2 * k] < 0:
                return False

        return True
