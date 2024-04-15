class Solution:
    def countOperationsToEmptyArray(self, nums: List[int]) -> int:
        size   = len(nums)
        result = size # all elements will be removed at some point

        # sort by value, track original position
        lookup = sorted([ ( n, i ) for i, n in enumerate(nums) ])
        # compare neighbors
        for (n1, i1), (n2, i2) in zip(lookup, lookup[1 :]):
            # shrink by one
            size -= 1

            # rotate array if wrong order
            if i1 > i2:
                result += size

        return result
