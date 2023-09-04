class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        result = 0

        found = defaultdict(list)
        sum = 0
        found[0] = [ -1 ]

        for i in range(len(nums)):
            sum += nums[i]
            found[sum].append(i)

        for f in found:
            if f + k in found:
                for left in found[f]:
                    right = bisect_right(found[f + k], left)
                    result += len(found[f + k]) - right

        return result
