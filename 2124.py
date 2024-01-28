class Solution:
    def checkString(self, s: str) -> bool:
        a = s.rfind("a")
        b = s. find("b")

        return b == -1 or b > a
