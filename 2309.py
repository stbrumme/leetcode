class Solution:
    def greatestLetter(self, s: str) -> str:
        freq = { "" }
        for c in s:
            freq.add(c)

        for c in range(25, -1, -1):
            high = chr(ord('A') + c)
            low  = chr(ord('a') + c)
            if high in freq and low in freq:
                return high

        return ""
