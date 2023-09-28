class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        chars = defaultdict(int)
        for c in s:
            chars[c] += 1

        ordered = []
        for c in chars:
            ordered.append(( c, chars[c] ))
        ordered.sort()

        result = ""
        useBest = True
        while ordered:
            if useBest:
                # pick as many letters as possible from the lexico largest
                letter, count = ordered[-1]
                if count > repeatLimit:
                    # enough letters left
                    result += letter * repeatLimit
                    ordered[-1] = (letter, count - repeatLimit)
                    useBest = False
                else:
                    # use anything left
                    result += letter * count
                    ordered.pop()
                    useBest = True
            else:
                # pick one letter from the lexico second largest
                if len(ordered) == 1: # no second-best
                    break

                letter, count = ordered[-2]
                result += letter
                useBest = True

                # decrement counter
                if count == 1:
                    ordered.pop(-2) # last letter
                else:
                    ordered[-2] = (letter, count - 1)

        return result
