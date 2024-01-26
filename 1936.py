class Solution:
    def addRungs(self, rungs: List[int], dist: int) -> int:
        result = 0

        rungs  = [ 0 ] + rungs
        height = 0
        pos    = 0
        while height < rungs[-1]:
            # find highest reachable rung
            next = bisect_right(rungs, height + dist, pos) - 1
            if next == len(rungs): # finished
                break

            # need extra rungs
            if next == pos:
                gap     = rungs[next + 1] - height
                result += (gap - 1) // dist
                next   += 1

            pos    = next
            height = rungs[next]

        return result
