class Solution:
    def reverseString(self, s: List[str]) -> None:
        r = s[::-1]
        for i in range(len(r)):
            s[i] = r[i]
