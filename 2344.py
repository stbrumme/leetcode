class Solution:
    def minOperations(self, nums: List[int], numsDivide: List[int]) -> int:
        result  = 0
        divisor = gcd(*set(numsDivide))

        heapify(nums)
        while nums and divisor % nums[0] != 0:
            heappop(nums)
            result += 1

        return result if nums else -1
