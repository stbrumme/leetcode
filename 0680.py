class Solution:
    def validPalindrome(self, s: str) -> bool:
        left  = 0
        right = len(s) - 1

        while left < right and s[left] == s[right]:
            left  += 1
            right -= 1
        if left >= right:
            return True

        # delete one on left side
        l, r = left+1, right        
        while l < r and s[l] == s[r]:
            l += 1
            r -= 1
        if l >= r:
            return True

        # delete one on right side
        l, r = left, right-1
        while l < r and s[l] == s[r]:
            l += 1
            r -= 1
        return l >= r