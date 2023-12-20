class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        # just four combinations, let's check them manually
        if s1 == s2:
            return True

        a,b,c,d = list(s1)
        if c+b+a+d == s2:
            return True
        if c+d+a+b == s2:
            return True
        if a+d+c+b == s2:
            return True

        return False
