class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        # popping from the end is much faster than from the beginning
        firstList  = list(reversed(firstList))
        secondList = list(reversed(secondList))
        while firstList and secondList:
            f1, f2 = firstList[-1]
            s1, s2 = secondList[-1]
            # remove uncrossed intervals
            if f2 < s1:
                firstList.pop()
                continue
            if s2 < f1:
                secondList.pop()
                continue

            # intersection
            i1 = max(f1, s1)
            i2 = min(f2, s2)
            yield i1, i2

            # remove if intersection completed "used" that interval
            if f2 <= i2:
                firstList .pop()
            if s2 <= i2:
                secondList.pop()
