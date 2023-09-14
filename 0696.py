class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        result = 0

        previous, same = 0, 1
        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                same   += 1
                result += (same <= previous)
            else:
                previous, same = same, 1
                result += 1

        return result
