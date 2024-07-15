class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        # only even lengths can produce balanced strings
        if len(s) & 1:
            return False

        # forward: at least as many "(" as ")"
        # always assume "(" if unlocked but if there too many "(" we can easily replace a few by ")"
        depth = 0
        for c, l in zip(s, locked):
            if l == "0" or c == "(":
                depth += 1
            else:
                depth -= 1
                if depth < 0:
                    return False

        # backward: same as before but at least as many ")" as "(" (reversed order)
        depth = 0
        for c, l in zip(reversed(s), reversed(locked)):
            if l == "0" or c == ")":
                depth += 1
            else:
                depth -= 1
                if depth < 0:
                    return False

        return True
