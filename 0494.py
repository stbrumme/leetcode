class Solution:
    def half(self, nums, target):
        size  = len(nums)
        mid   = size // 2
        left  = nums[:mid]
        right = nums[mid:]

        limit = 2 ** mid
        current = 0
        leftSum = defaultdict(int)
        for current in range(limit):
            have = 0
            mask = limit
            for j in range(mid):
                mask >>= 1
                if (current & mask) == 0:
                    have += left[j]
                else:
                    have -= left[j]
            leftSum[have] += 1

        limit = 2 ** (size - mid)
        current = 0
        rightSum = defaultdict(int)
        for current in range(limit):
            have = 0
            mask = limit
            for j in range(size - mid):
                mask >>= 1
                if (current & mask) == 0:
                    have += right[j]
                else:
                    have -= right[j]
            rightSum[have] += 1

        result = 0
        for l in leftSum:
            howOften = leftSum[l]
            need = target - l
            if need in rightSum:
                result += howOften * rightSum[need]
        return result


    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        size = len(nums)
        if size > 5:
            return self.half(nums, target)

        nums.sort(reverse = True)
        total = sum(nums)

        remaining = [0] * size
        for i in range(size):
            total -= nums[i]
            remaining[i] = total

        loops = 0

        result = 0
        limit = 2**size
        current = 0
        while current < limit:
            have = 0
            mask = limit
            for j in range(size):
                mask >>= 1
                if (current & mask) == 0:
                    have += nums[j]
                else:
                    have -= nums[j]

                need = target - have
                # already too big or too small ?
                if need > +remaining[j] or need < -remaining[j]:
                    current += mask - 1
                    break

            if have == target:
                result += 1

            current += 1
            loops += 1

        return result
