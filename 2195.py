class Solution:
    def minimalKSum(self, nums: List[int], k: int) -> int:
        limit = k
        skip  = 0
        for n in sorted(set(nums)): # skip duplicates
            # extend range
            if n <= limit:
                limit += 1
                skip  += n
            else:
                break

        return limit * (limit + 1) // 2 - skip
