class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        # breadth-first search
        todo = [ s ]
        stop = False # becomes True after first valid string found
        while not stop:
            next = set()

            for t in todo:
                # check if brackets match
                depth = 0
                for c in t:
                    if   c == "(":
                        depth += 1
                    elif c == ")":
                        depth -= 1
                        if depth < 0: # "underflow"
                            break

                # we have a match, stop after this round
                if depth == 0:
                    stop = True
                    yield t
                    continue

                # keep going ...
                for i, c in enumerate(t):
                    if c in "()": # always keep letters, remove only parentheses
                        shorter = t[: i] + t[i + 1:]
                        next.add(shorter)

            todo = next
