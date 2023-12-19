class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        zero = s.count("0")
        if zero == 0 or zero == len(s):
            return 0

        result = inf
        if s[0] == "1":
            result = zero

        ones   = 0
        for c in s:
            if c == "0":
                zero -= 1
            else:
                ones += 1

            result = min(result, zero + ones)

        return result
