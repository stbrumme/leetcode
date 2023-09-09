class Solution:
    # see problem 227
    def calculate(self, s: str) -> int:
        s = s.replace(" ", "") # discard spaces
        s += "?"               # end-marker

        num    = 0
        sum    = 0
        minus  = False
        negate = [ minus ]
        # no brackets, almost sequential evaluation possible
        # note: * and / have hive precedence than + and -
        for c in s:
            if c.isnumeric():
                num = 10 * num + int(c)
            elif c == "(":
                negate.append(minus)
            elif c == ")":
                negate.pop()
            else: # "+", "-", "?"
                sum += -num if minus else +num
                num  = 0
                minus = (c == "-")
                if negate[-1] == True:
                    minus = not minus

        return sum
