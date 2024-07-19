class Solution:
    def minSpaceWastedKResizing(self, nums: List[int], k: int) -> int:
        size = len(nums)

        # for each range [left, right]: compute minimum waste if not resized
        # that means the available space must be the maximum value
        @cache
        def chunk(left, right):
            # not very efficient ...
            data  = nums[left : right + 1]
            width = right - left + 1
            return max(data) * width - sum(data)

        @cache
        def deeper(pos, k):
            if pos == size:
                return 0
            if k == 0:
                return chunk(pos, size - 1)

            best = chunk(pos, size - 1)
            for split in range(pos, size):
                best = min(best, chunk(pos, split) + deeper(split + 1, k - 1))
            return best

        return deeper(0, k)
