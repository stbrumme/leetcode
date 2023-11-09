class Solution:
    def countHomogenous(self, s: str) -> int:
        result = 0

        prev = ""
        same = 1
        for c in s:
            if prev == c:
                same += 1
            else:
                same  = 1
                prev  = c

            result += same

        return result % 1_000_000_007
