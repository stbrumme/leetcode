class Solution:
    def maximizeSquareArea(self, m: int, n: int, hFences: List[int], vFences: List[int]) -> int:
        # trivial case: remove all fences
        if m == n:
            return (m - 1) ** 2

        # find all (unique) possible distances between fences
        def gaps(fences):
            result = set()

            size = len(fences)
            for i in range(size):
                for j in range(i):
                    result.add(fences[i] - fences[j])

            return result

        # add borders as virtual fences, too
        h = gaps([1] + sorted(hFences) + [ m ])
        v = gaps([1] + sorted(vFences) + [ n ])

        # find largest gap present in both arrays
        both = h.intersection(v)
        return (max(both) ** 2) % 1_000_000_007 if both else -1
