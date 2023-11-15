class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:
        result = 0

        # simply brute force
        # plsu a few checks for len() to reduce string operations
        for i in range(len(nums)):
            n = nums[i]
            if len(n) >= len(target):
                continue

            for j in range(len(nums)):
                if i != j:
                    m = nums[j]
                    if len(n) + len(m) == len(target) and n + m == target:
                        result += 1
        return result
