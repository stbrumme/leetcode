class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        complete = []
        for left, right in sorted(intervals):
            if complete and complete[0] < left:
                # attach to an existing group
                heappushpop(complete, right)
            else:
                # start a new group
                heappush   (complete, right)

        return len(complete)
