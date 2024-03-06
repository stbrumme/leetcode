class Solution:
    def minimumLength(self, s: str) -> int:
        left  = 0
        right = len(s) - 1

        while left < right and s[left] == s[right]:
            what = s[left]

            # prefix
            while left <= right and s[left]  == what:
                left  += 1
            # suffix
            while left <= right and s[right] == what:
                right -= 1

        return right - left + 1
