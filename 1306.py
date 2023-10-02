class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        need = set([ i for i,a in enumerate(arr) if a == 0 ])
        have = set()
        todo = set([ start ])
        while todo:
            next = set()
            for t in todo:
                if t in have:
                    continue
                have.add(t)

                if t in need:
                    return True

                if t - arr[t] >= 0:
                    next.add(t - arr[t])
                if t + arr[t] < len(arr):
                    next.add(t + arr[t])

            todo = next

        return False
