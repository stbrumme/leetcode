class Solution:
    def checkValidString(self, s: str) -> bool:
        @cache
        def deeper(pos, depth):
            # mismatch
            if depth < 0:
                return False

            # end of input
            if pos == len(s):
                return depth == 0

            c = s[pos]
            if c == "(":
                return deeper(pos + 1, depth + 1)
            if c == ")":
                return deeper(pos + 1, depth - 1)

            # must be "*", try to replace it by "", "(" or ")"
            return deeper(pos + 1, depth)     or \
                   deeper(pos + 1, depth + 1) or \
                   deeper(pos + 1, depth - 1)

        return deeper(0, 0)
