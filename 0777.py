class Solution:
    def canTransform(self, start: str, end: str) -> bool:
        # L and R must retain their order
        # verify it by removing any Xs
        if start.replace("X", "") != end.replace("X", ""):
            return False

        r1 = [ i for i, c in enumerate(start) if c == "R" ]
        r2 = [ i for i, c in enumerate(end)   if c == "R" ]
        l1 = [ i for i, c in enumerate(start) if c == "L" ]
        l2 = [ i for i, c in enumerate(end)   if c == "L" ]

        if len(r1) != len(r2):
            return False
        # now len(l1) == len(l2), too

        # "R" can't move left
        for a, b in zip(r1, r2):
            if a > b:
                return False

        # "L" can't move right
        for a, b in zip(l1, l2):
            if a < b:
                return False

        return True
