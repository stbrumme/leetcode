class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        if k == 1:
            return True
        if k > len(nums):
            return False

        freq = defaultdict(int)
        for n in nums:
            freq[n] += 1

        keys = list(sorted(freq))
        for f in keys:
            need = freq[f]
            if need > 0:
                for i in range(f, f + k):
                    freq[i] -= need
                    if freq[i] < 0:
                        return False

        return True
