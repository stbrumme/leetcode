class Solution:
    def removePalindromeSub(self, s: str) -> int:
        # empty
        if not s:
            return 0

        # palindrome
        if s == s[::-1]:
            return 1

        # 1. generate a subsequence consisting of a's only => that's a palindrome, remove it
        # 2. only b's are left => that's a palindrome, too, can be removed
        return 2
