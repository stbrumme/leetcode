class Solution:
    def minimumMoves(self, s: str) -> int:
        result = 0
        pos    = 0
        while pos < len(s):
            if s[pos] == "X":
                # apply "stamp" whenever we see three characters where the first is an X
                # and then skip the next two
                result += 1
                pos    += 3
            else:
                pos    += 1
        return result
