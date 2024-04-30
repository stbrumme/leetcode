class Solution:
    def minOperations(self, nums: List[int]) -> int:
        result = +inf
        size   = len(nums)

        # make sure at least one element is 1
        # then "spread" this value
        one = nums.count(1)
        if one > 0:
            return size - one

        # check if impossible
        if gcd(*nums) > 1:
            return -1

        # find shortest way to reach 1
        for i in sorted(range(size), key = lambda x : nums[x]): # try to find short sequences early (and exit)
            have = nums[i]
            for length, next in enumerate(nums[i + 1 :]):
                have = gcd(have, next)
                if have == 1:
                    result = min(result, length + size)
                    if result == 2: # early exit
                        return result

        return result
