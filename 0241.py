class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        @cache
        def deeper(s):
            if s.isnumeric():
                return [ int(s) ]

            result = []
            for i in range(len(s)):
                if s[i] in [ "+", "-", "*"]:
                    left  = deeper(s[:i])
                    right = deeper(s[i+1:])
                    for l in left:
                        for r in right:
                            if   s[i] == "+":
                                result.append(l + r)
                            elif s[i] == "-":
                                result.append(l - r)
                            elif s[i] == "*":
                                result.append(l * r)

            return result

        return deeper(expression)
