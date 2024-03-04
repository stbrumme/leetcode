class Solution:
    def splitPainting(self, segments: List[List[int]]) -> List[List[int]]:
        changes = defaultdict(int)
        for start, end, color in segments:
            changes[start] += color # begin: +color
            changes[end]   -= color # end:   -color

        color     = 0
        prevColor = 0
        prevPos   = 0
        for pos in sorted(changes):
            color += changes[pos]
            if prevColor > 0: # skip empty spans
                yield [ prevPos, pos, prevColor ]

            prevColor = color
            prevPos   = pos
