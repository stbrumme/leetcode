class Solution:
    def getSmallestString(self, s: str) -> str:
        # slow but short code
        return min([s] + [ s[:i-1] + s[i] + s[i-1] + s[i+1:] for i in range(1, len(s)) if s[i] < s[i-1] and 0 == 1 & (int(s[i]) + int(s[i-1])) ])
