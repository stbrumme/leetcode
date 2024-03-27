class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        # the math behind my solution:
        # if   sum([a,b]) % k == sum([a,b,c,d]) % k
        # then sum([c,d]) % k == 0

        # store position of the first time we observe a modulo
        modulo = { }

        total = 0
        for i, n in enumerate(nums):
            total += n
            group  = total % k

            # a good subarray could start with the very first element
            if group == 0 and i >= 1:
                return True

            # we had the same modulo
            if group in modulo:
                # but good subarrays have at least 2 elements
                if i - modulo[group] >= 2:
                    return True
            else:
                modulo[group] = i

        # the whole input may be good, after all
        return False
