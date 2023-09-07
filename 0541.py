class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        for left in range(0, len(s), 2*k):
            right = left + k

            rev = s[left:right]
            rev = rev[::-1] # reverse
            s = s[:left] + rev + s[right:]

        return s
