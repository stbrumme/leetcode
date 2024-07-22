class Solution:
    def minimumCost(self, m: int, n: int, horizontalCut: List[int], verticalCut: List[int]) -> int:
        result = 0

        # if a horizontal cut took place first,
        # then any vertical cut's price doubled
        # because each such vertical cut needs to be done twice

        # the same logic applies when you start with a vertical cut
        # and follow up with horizontal cuts

        # perform expensive cuts first before their price doubles
        horizontalCut.sort(reverse = True)
        verticalCut  .sort(reverse = True)

        # stopmarker
        horizontalCut.append(0)
        verticalCut  .append(0)

        h = v = 0 # index for horizontalCut/verticalCut

        # perform all cuts, most expensive first
        while horizontalCut[h] > 0 or verticalCut[v] > 0:
            if horizontalCut[h] > verticalCut[v]:
                result += horizontalCut[h] * (v + 1)
                h      += 1
            else:
                result += verticalCut[v] * (h + 1)
                v      += 1

        return result
