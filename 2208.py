class Solution:
    def halveArray(self, nums: List[int]) -> int:
        have = sum(nums)
        need = have / 2

        steps = 0
        ordered = [ -n for n in nums ] # max-heap
        heapify(ordered)
        while have > need:
            half  = -ordered[0] / 2
            have -= half
            heappushpop(ordered, -half)

            steps += 1

        return steps
