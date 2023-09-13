class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        # interview all candidates in every round
        if len(costs) <= candidates+candidates:
            s = sorted(costs)
            return sum(s[:k])

        # two heaps
        left  = costs[:candidates]
        mid   = costs[candidates:-candidates]
        right = costs[-candidates:]
        heapify(left)
        heapify(right)

        hired = []
        while len(hired) < k and mid:
            if left[0] <= right[0]:
                hired.append(heapreplace(left,  mid.pop(0)))
            else:
                hired.append(heapreplace(right, mid.pop(-1)))

        # heaps meet
        need = k - len(hired)
        if need > 0: # len(mid) == 0
            both = sorted(left + right)
            hired += both[:need]

        return sum(hired)
