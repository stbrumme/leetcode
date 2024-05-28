class Solution:
    def findMinStep(self, board: str, hand: str) -> int:
        result = +inf

        # remove clusters of three of more consecutive letters
        def remove(s):
            size = len(s)
            for i in range(size):
                j = i + 1
                # count identical cells
                while j < size and s[i] == s[j]:
                    j += 1

                same = j - i
                if same >= 3:
                    return remove(s[ : i] + s[j : ])
            return s

        @cache
        def deeper(b, h, depth = 0): # board, hand
            nonlocal result
            if depth >= result:
                return

            # finished board ?
            b = remove(b)
            if not b:
                result = depth
                return

            # insert each kind of ball
            for insert in h:
                nexthand = h.replace(insert, "", 1)

                # insert at the end
                deeper(b + insert, nexthand, depth + 1)
                deeper(b[ : -1] + insert + b[-1], nexthand, depth + 1) # dirty hack for "RRWWRRBBRR", "WB"
                # insert to the left of a ball with the same color
                for i in range(len(b)):
                    if b[i] == insert:
                        deeper(b[ : i] + insert + b[i : ], nexthand, depth + 1)
                    else:
                        if len(set(h)) < 3: # dirty hack for "RRYRRYYRYYRRYYRR", "YYRYY"
                            deeper(b[ : i] + insert + b[i : ], nexthand, depth + 1)

        deeper(board, hand)
        return result if result != +inf else -1
