class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        result = 0

        allOdd = allEven = 0 # sum of all odd or even numbers
        for i, n in enumerate(nums):
            if i & 1:
                allOdd  += n
            else:
                allEven += n

        odd = even = 0
        for i, n in enumerate(nums):
            # left side of i
            a = odd
            b = even

            if i & 1:
                odd  += n
            else:
                even += n

            # right side of i
            a += allEven - even
            b += allOdd  - odd

            # fair ?
            if a == b:
                result += 1

        return result
