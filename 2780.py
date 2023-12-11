class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        size = len(nums)
        dominant = None

        freq = defaultdict(int)
        for n in nums:
            freq[n] += 1
            if freq[n] * 2 > size:
                dominant = n

        left  = 0
        right = freq[dominant]
        for i, n in enumerate(nums):
            # split after i
            pos = i + 1
            if n == dominant:
                # shift a dominant element from right to left partition
                left  += 1
                right -= 1
                if left * 2 > pos and right * 2 > (size - pos):
                    return pos - 1
        return -1
