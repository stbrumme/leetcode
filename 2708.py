class Solution:
    def maxStrength(self, nums: List[int]) -> int:
        # remove all zeros
        nonzero = [ n for n in nums if n != 0 ]
        if not nonzero:
            return 0

        # single number
        if len(nonzero) == 1:
            return max(nums) # if nonzero[0] is negative, then use potential zeros in nums

        result   = 1
        negative = []
        for n in nonzero:
            if n > 0: # all positive scores belong to the group
                result *= n
            else:
                negative.append(n)

        # an even number of negative scores belong to the group, too
        negative.sort()
        if len(negative) & 1:
            negative.pop() # remove the largest if odd size

        return result * prod(negative)
