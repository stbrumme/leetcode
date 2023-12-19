class Solution:
    def ambiguousCoordinates(self, s: str) -> List[str]:
        # remove brackets
        s = s[1:-1]

        # return list of possible numbers (as strings)
        def versions(text):
            if not text:
                return []

            if len(text) == 1:
                return [ text ]

            if text[-1] == "0":
                # must be an integer
                return [] if text[0] == "0" else [ text ]

            if text[0] == "0":
                # must be floating-point
                return [ "0." + text[1:] ]

            result = [ text ]
            # place dots
            for i in range(1, len(text)):
                result.append(text[:i] + "." + text[i:])
            return result

        for i in range(1, len(s)):
            one = versions(s[:i])
            two = versions(s[i:])
            for o in one:
                for t in two:
                    yield "(" + o + ", " + t + ")"
