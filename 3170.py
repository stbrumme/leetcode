class Solution:
    def clearStars(self, s: str) -> str:
        seen   = [] # min-heap of character, max-heap of position
        delete = set() # index of deleted characters
        for i, c in enumerate(s):
            if c == "*":
                # delete most recent occurrence of the smallest character
                _, pos = heappop(seen)
                delete.add(-pos)
            else:
                heappush(seen, ( c, -i ))

        result = [ c for i, c in enumerate(s) if c != "*" and i not in delete ]
        return "".join(result)
