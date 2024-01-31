class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        result = +inf

        size = len(nums)
        for i in range(size):
            a = nums[i]
            for j in range(i + 1, size):
                b = nums[j]
                if a < b:
                    for k in range(j + 1, size):
                        c = nums[k]
                        if b > c:
                            result = min(result, a + b + c)

        return -1 if result == +inf else result
