class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False

        LAST = "|"
        s1 += LAST
        s2 += LAST

        @cache
        def deeper(a, b):
            c = a + b
            if c == len(s3):
                return True

            if s3[c] == s1[a] and s3[c] == s2[b]:
                return deeper(a+1, b) or deeper(a, b+1)
            if s3[c] == s1[a]:
                return deeper(a+1, b)
            if s3[c] == s2[b]:
                return deeper(a, b+1)
            return False

        return deeper(0, 0)
