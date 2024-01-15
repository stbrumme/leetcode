class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        result = 0

        todo = []
        for a, b in intervals:
            heappush(todo, (a, -b)) # sort by start (ascending), then end (descending)

        covered = 0 # end of already covered interval
        while todo:
            a, b = heappop(todo)
            b = -b # was inserted negated to enforce descending order
            if b > covered:
                result += 1
                covered = b

        return result
