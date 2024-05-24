class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        result = 0

        # remove the pattern, return score and cleaned up text
        def match(text, a, b, score):
            # basic check to avoid only a or only b
            same = sum(text)
            if same == 0 or same == len(text):
                return ( 0, text )

            result = 0
            seen   = [] # stack
            for c in text:
                #if seen and seen[-1] == a and c == b:
                if c == b and seen and seen[-1] == a:
                    result += score
                    seen.pop()
                else:
                    seen.append(c)
            return ( result, seen )

        def score(segment):
            # process the higher-valued substring first
            if x >= y:
                ab, next = match(segment, 0, 1, x) # "ab"
                ba, _    = match(next,    1, 0, y) # "ba"
            else:
                ba, next = match(segment, 1, 0, y) # "ba"
                ab, _    = match(next,    0, 1, x) # "ab"

            return ab + ba

        # split into segments only consisting of a and b
        have = []
        for c in s + "!": # stop marker so that the final segment is properly handled, too
            if c in "ab":
                have.append(0 if c == "a" else 1)
            elif have:
                result += score(have)
                have    = []

        return result
