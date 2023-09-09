class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        rev  = False
        flat = []
        while board:
            last  = board.pop()
            flat += reversed(last) if rev else last
            rev   = not rev
        size = len(flat)

        flat = [ None ] + flat + [ -1 ] * 6 # make it one-based and simplify out-of-range checks

        have = set()
        todo = set([ 1 ])
        steps = 0
        while todo:
            next = set()
            for t in todo:
                if t >= size:
                    return steps

                if t in have:
                    continue
                have.add(t)

                for roll in range(t+1, t+1+6):
                    next.add(roll if flat[roll] == -1 else flat[roll])

            steps += 1
            todo = next

        return -1
