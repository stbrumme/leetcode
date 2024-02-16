class Solution:
    def findKOr(self, nums: List[int], k: int) -> int:
        bits = 31
        freq = [ 0 ] * bits
        for n in nums:
            for i in range(bits):
                if n & (1 << i):
                    freq[i] += 1

        result = 0
        for i in range(bits):
            if freq[i] >= k:
                result |= 1 << i
        return result
