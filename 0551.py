class Solution:
    def checkRecord(self, s: str) -> bool:
        # let's do it the very tricky way ...
        return s.find("LLL") == s.find("A", 1 + s.find("A"))
