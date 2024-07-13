class Solution:
    def makeSimilar(self, nums: List[int], target: List[int]) -> int:
        # "similar" means that the arrays are equal if sorted
        # changing by +2/-2 keeps the parity (odd will stay odd, even will stay even)

        result = 0
        for parity in ( 0, 1 ):
            # sorting keeps the absolute difference low
            one = sorted(n for n in nums   if (n & 1) == parity)
            two = sorted(t for t in target if (t & 1) == parity)

            result += sum(abs(a - b) >> 1 for a, b in zip(one, two))

        return result >> 1
