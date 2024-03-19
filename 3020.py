class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        freq = defaultdict(int)
        for n in nums:
            freq[n] += 1

        @cache
        def deeper(n):
            # nope
            if n not in freq:
                return 0

            # special case 1^n = 1, avoid endless recursion
            if n == 1:
                return (freq[1] + 1) // 2

            # if only found once element, then it must be the middle element / peak
            if freq[n] == 1:
                return 1

            # freq[n] > 1, keep going
            return 1 + deeper(n * n)

        # deeper() computes only half of the subset
        return max(deeper(n) for n in sorted(freq)) * 2 - 1
