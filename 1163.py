class Solution:
    def lastSubstring(self, s: str) -> str:
        result = ""

        # first letter
        first  = max(s)
        pos    = s.find(first)
        while pos != -1:
            result = max(result, s[pos : ])
            pos    = s.find(first, pos + 1)

        return result
