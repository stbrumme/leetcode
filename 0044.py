class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        @cache
        def match(posS, posP):
            if posS == len(s) and posP == len(p):
                return True
            if posP == len(p):
                return False

            # wildcards
            if p[posP] == "?":
                if posS == len(s):
                    return False
                return match(posS + 1, posP + 1)

            if p[posP] == "*":
                for i in range(posS, len(s) + 1):
                    if match(i, posP + 1):
                        return True
                return False

            if posS == len(s):
                return False

            # same letters
            if p[posP] == s[posS]:
                return match(posS + 1, posP + 1)

            return False

        return match(0, 0)
