class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        state = [ d for d in dominoes ]
        left  = set([ i for i, d in enumerate(dominoes) if d == "L" ])
        right = set([ i for i, d in enumerate(dominoes) if d == "R" ])

        while right or left:
            nextright = set()
            for r in right:
                if r + 1 in left:
                    left.discard(r + 1)
                    continue
                if r + 2 in left:
                    left.discard(r + 2)
                    continue
                if r + 1 not in right and r + 1 < len(state) and state[r + 1] == ".":
                    nextright.add(r + 1)
                    state[r + 1] = "R"

            nextleft = set()
            for l in left:
                if l - 1 not in left and l > 0 and state[l - 1] == ".":
                    nextleft.add(l - 1)
                    state[l - 1] = "L"

            left  = nextleft
            right = nextright

        return "".join(state)
