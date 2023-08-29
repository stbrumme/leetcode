class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        @cache
        def deeper(left, right):
            if left > right:
                return 0

            # single character is palindrome, too
            if left == right:
                return 1
            # matching pair
            if s[left] == s[right]:
                return 2 + deeper(left+1, right-1)

            return max(deeper(left+1, right), deeper(left, right-1))

        return deeper(0, len(s) - 1)
