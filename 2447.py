class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        result = 0
        size   = len(nums)

        for i in range(size):
            have = nums[i]

            for j in range(i, size):
                more = nums[j]
                have = gcd(have, more)

                # GCD of a list can't grow if adding more elements
                if have <  k:
                    break

                # match
                if have == k:
                    result += 1

        return result
