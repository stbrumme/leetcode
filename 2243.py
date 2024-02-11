class Solution:
    def digitSum(self, s: str, k: int) -> str:
        if len(s) <= k:
            return s

        next = ""
        while s:
            x = s[:k]
            s = s[k:]

            x = int(x)
            dsum = 0
            while x > 0:
                dsum += x % 10
                x   //= 10
            next += str(dsum)

        return self.digitSum(next, k)
