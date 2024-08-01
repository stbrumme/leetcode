class Solution:
    def maxBuilding(self, n: int, restrictions: List[List[int]]) -> int:
        result = 0

        limits = { pos : height for pos, height in restrictions }
        # additional restrictions:
        # - first building has height 0
        # - last  building has at most height n - 1
        limits[1] = 0
        if n not in limits:
            limits[n] = n # needed to properly handle the last building

        known = sorted(limits)
        # reduce limits of buildings on the right side
        for a, b in zip(known, known[1 :]):
            gap = b - a
            limits[b] = min(limits[b], limits[a] + gap)
        # reduce limits of buildings on the left  side
        for a, b in zip(reversed(known[ : -1]), reversed(known)):
            gap = b - a
            limits[a] = min(limits[a], limits[b] + gap)

        # highest point
        for a, b in zip(known, known[1 :]):
            gap  = b - a
            high = max(limits[a], limits[b])
            diff = abs(limits[a] - limits[b]) # height difference
            result = max(result, high + (gap - diff) // 2)

        return result
