class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        insert = 0

        # nesting must never be negative
        nesting = 0
        for c in s:
            if c == "(":
                nesting += 1
            else:
                nesting -= 1
                if nesting < 0:
                    nesting = 0
                    insert += 1

        return insert + nesting # close open brackets, too
