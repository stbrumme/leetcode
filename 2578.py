class Solution:
    def splitNum(self, num: int) -> int:
        s = sorted(str(num))

        a = ""
        b = ""
        for i in range(len(s)):
            if i & 1:
                a += s[i]
            else:
                b += s[i]

        return int(a) + int(b)
