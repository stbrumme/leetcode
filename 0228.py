class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []

        nums.append(2**100)
        result = []

        left = right = nums[0]
        for i in range(1, len(nums)):
            n = nums[i]
            if n == right + 1:
                right = n
            else:
                if left == right:
                    result.append(str(left))
                else:
                    result.append(str(left) + "->" + str(right))

                left = right = nums[i]

        return result
