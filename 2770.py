class Solution:
    def maximumJumps(self, nums: List[int], target: int) -> int:
        last = len(nums) - 1
        step = [ -inf ] * last + [ 0 ]
        have = [ ( n, i ) for i, n in enumerate(nums) ]
        have.sort()

        for i in reversed(range(last)):
            left  = bisect_left (have, ( nums[i] - target, i ))
            right = bisect_right(have, ( nums[i] + target, last ))
            best  = -inf
            for value, pos in have[left : right]:
                if pos > i:
                    best = max(best, 1 + step[pos])
            step[i] = best

        return step[0] if step[0] > 0 else -1
