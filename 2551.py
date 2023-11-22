class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        # edge case: one bag
        if k == 1:
            return 0

        # split marbles into k consecutive groups
        # cost of each bag is weight[i] + weight[j]
        # each split after index x will add weight[x] and weight[x+1] to the total cost:
        # weight[x]   because it's the last  index of one      bag
        # weight[x+1] because it's the first index of the next bag

        borders = [ weights[x] + weights[x + 1] for x in range(len(weights) - 1) ]
        borders.sort()

        # don't forget about weight[0] and weight[-1]
        ends = weights[0] + weights[-1]
        # in the end there are k-1 splits for k bags
        splits = k - 1

        low  = ends + sum(borders[:splits])
        high = ends + sum(borders[-splits:])

        # actually there is no need for "ends" because it will be eliminated ...
        return high - low
