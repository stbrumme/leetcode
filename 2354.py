class Solution:
    def countExcellentPairs(self, nums: List[int], k: int) -> int:
        result = 0

        # on bit level:
        # (0 OR 0) + (0 AND 0) = 0
        # (0 OR 1) + (0 AND 1) = 1
        # (1 OR 0) + (1 AND 0) = 1
        # (1 OR 1) + (1 AND 1) = 2

        # that means:
        # (a OR b) + (a AND b) = a + b
        # it can be extended to whole integers, too
        # therefore ( x, y ) is excellent if x.bit_count() + y.bit_count() >= k

        # ensure all pairs are distinct
        nums = set(nums)
        bits = [ 0 ] * 30 # 2^30 > 10^9
        for n in nums:
            bits[n.bit_count()] += 1

        # strip unused high bits
        while bits and bits[-1] == 0:
            bits.pop()
        size = len(bits)

        # count pairs where sum of bits >= k
        for a in range(size):
            for b in range(size):
                if a + b >= k:
                    result += bits[a] * bits[b]

        return result
