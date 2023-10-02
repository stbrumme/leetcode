class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        result = [ -1 ] * n
        result[0] = 0

        r = defaultdict(set)
        for src, dst in redEdges:
            r[src].add(dst)

        b = defaultdict(set)
        for src, dst in blueEdges:
            b[src].add(dst)

        red  = r[0]
        blue = b[0]

        seenRed  = set()
        seenBlue = set()

        steps = 1
        while red or blue:
            nextRed  = set()
            nextBlue = set()

            for current in red:
                if current in seenRed:
                    continue

                seenRed.add(current)
                if result[current] == -1:
                    result[current] = steps

                nextBlue |= b[current]

            for current in blue:
                if current in seenBlue:
                    continue

                seenBlue.add(current)
                if result[current] == -1:
                    result[current] = steps

                nextRed |= r[current]

            steps += 1
            red    = nextRed
            blue   = nextBlue

        return result
