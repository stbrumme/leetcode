class Solution:
    def minimumOperationsToMakeEqual(self, x: int, y: int) -> int:
        # edge case
        if x <= y:
            return y - x # always +1

        have  = set()
        todo  = [ x ]
        steps = 0
        while todo:
            next = set()

            for t in todo:
                if t == y:
                    return steps

                have.add(t)

                # helper function: store only new values
                def add(x):
                    if x not in have:
                        next.add(x)

                if t < x + 11: # reach the next multiple of 11
                    add(t + 1)
                if t > y:
                    add(t - 1)
                    if t % 11 == 0:
                        add(t // 11)
                    if t %  5 == 0:
                        add(t //  5)

            todo   = next
            steps += 1
