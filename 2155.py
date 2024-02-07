class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        result = [ 0 ]

        size = len(nums)
        zero = 0
        ones = sum(nums)
        high = ones

        # degenerated cases
        if ones == 0:
            return [ size ]
        if ones == size:
            return [ 0 ]

        for i, n in enumerate(nums):
            split = i + 1

            # update counters
            if n == 0:
                zero += 1
            else:
                ones -= 1

            score = zero + ones
            if   high < score:
                # new highscore
                high = score
                result = [ split ]
            elif high == score:
                # same highscore
                result.append(split)

        return result
