class Solution:
    def makeSubKSumEqual(self, arr: List[int], k: int) -> int:
        result = 0
        size   = len(arr)
        # sum(a1,a2,...,ak) = sum(a0,a1,...,ak-1)
        # therefore a0 = ak

        # input values are never zero,
        # use zero as a placeholder for "already processed"
        for i in range(size):
            if arr[i] == 0:
                continue

            ring = []
            while arr[i] > 0:
                ring.append(arr[i])
                arr[i] = 0 # set placeholder
                i += k     # jump ahead
                i %= size  # and wraparound

            med     = int(statistics.median(ring))
            result += sum(abs(r - med) for r in ring)

        return result
