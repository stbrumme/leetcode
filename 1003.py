class Solution:
    def isValid(self, s: str) -> bool:
        incomplete = [] # stack

        for c in s:
            if   c == "a":
                incomplete.append(c)
            elif c == "b":
                # stack must be preceded by "a"
                if not incomplete:
                    return False
                if incomplete[-1] != "a":
                    return False
                incomplete.append(c)
            else: # c == "c"
                # stack must be preceded by "ab"
                if len(incomplete) < 2:
                    return False
                if incomplete.pop() != "b":
                    return False
                if incomplete.pop() != "a":
                    return False

        return not incomplete
