class Solution:
    def waysToReachStair(self, k: int) -> int:
        # small inputs
        if k <= 1:
            return 2 if k == 0 else 4

        result = 0
        todo   = { 0: 1, 1: 1 } # initial stair and go one step back
                                # (these are all possible state with jump == 0)
        jump   = 1
        while todo:
            next = defaultdict(int)
            for n, count in todo.items():
                up = n + jump
                if up - 1 <= k:
                    next[up    ] += count # jump up
                    next[up - 1] += count # jump up and immediately go back one step back

            jump *= 2
            todo  = next

            # reached final stair
            result += todo.get(k, 0) # todo[k] creates a new key if k is missing
                                     # which doesn't work with my "while todo" loop

        return result
