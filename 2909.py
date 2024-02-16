class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        invalid = +inf
        result  = invalid
        size    = len(nums)

        # smallest nums[k], going from right to left
        right = [ ( size, +inf) ] # minheap: ( position, minimum )
        for k in reversed(range(size)):
            if nums[k] < right[0][1]:
                heappush(right, ( k, nums[k] ))

        # two jobs at once:
        # 1) track smallest nums[i], going from left to right
        # 2) check for each value whether it's bigger than left and right[i]
        #    => store their minimum sum
        left = nums[0]
        for i in range(size):
            if right[0][0] < i:
                heappop(right)

            left = min(left, nums[i])
            if left < nums[i] > right[0][1]:
                total = left + nums[i] + right[0][1]
                result = min(result, total)

        return result if result < invalid else -1
