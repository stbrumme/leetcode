class Solution:
    def sumDigitDifferences(self, nums: List[int]) -> int:
        result = 0

        # count digits for each position
        size   = len(str(nums[0]))
        have   = [ [ 0 ] * 10 for _ in range(size) ]
        total  = [ 0 ] * size # total[i] = sum(have[i])

        for n in nums:
            for pos in range(size):
                last = n % 10
                n  //= 10

                # sum of digits not identical to the current
                result += total[pos] - have[pos][last]

                have[pos][last] += 1
                total[pos]      += 1

        return result
