class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        while True:
            before = len(s)
            s = s.replace(part, "", 1)
            after  = len(s)
            if before == after:
                return s
