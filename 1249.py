class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        # emit at most as many "one" as "two"
        def filter(s, one, two):
            have = 0
            for c in s:
                if   c == one:
                    have += 1
                elif c == two:
                    if have == 0:
                        continue # skip
                    have -= 1

                yield c

        open  = filter(s,                    "(", ")") # left-to-right "()"
        close = filter(reversed(list(open)), ")", "(") # right-to-left ")("

        return "".join(reversed(list(close)))
