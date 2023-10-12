class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        return s.find("01") == -1
