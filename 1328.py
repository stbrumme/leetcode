class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        # always palindrome
        if len(palindrome) == 1:
            return ""

        # don't replace "a" if in the middle (=> will still be a palindrome)
        mid = -1
        if len(palindrome) & 1:
            mid = len(palindrome) // 2

        # look for first position which isn't "a"
        for i, c in enumerate(palindrome):
            if c > "a" and i != mid:
                return palindrome[:i] + "a" + palindrome[i + 1:]

        # only "a"s
        return palindrome[:-1] + "b"
