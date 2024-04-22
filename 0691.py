class Solution:
    def minStickers(self, stickers: List[str], target: str) -> int:
        candidates = defaultdict(set)
        for s in stickers:
            for c in s:
                candidates[c].add(s)

        # pre-check: all letters of target must be in candidates
        for t in target:
            if t not in candidates:
                return -1

        # lots of type conversions required ...
        todo  = [ tuple(list(target)) ]
        steps = 0
        stop  = False
        while not stop:
            steps += 1
            next   = set()

            for t in todo:
                need = t[0]

                for c in candidates[need]:
                    less = list(t)
                    # strip letters provided by current candidate
                    for x in c:
                        if x in less:
                            less.pop(less.index(x))

                    if less:
                        # next round
                        next.add(tuple(less))
                    else:
                        # we're done
                        stop = True
                        break

            todo = next

        return steps
