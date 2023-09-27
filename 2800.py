class Solution:
    def minimumString(self, a: str, b: str, c: str) -> str:
        # merge x and y (the result for y and x might be different !)
        def combine(x, y):
            # y is part of x
            if x.find(y) != -1:
                return x

            # longest overlap
            shared = min(len(x), len(y))
            for i in range(shared - 1, 0, -1):
                if x[-i:] == y[:i]:
                    return x + y[i:]

            # no overlap
            return x + y

        candidates = []
        candidates.append(combine(combine(a, b), c))
        candidates.append(combine(combine(a, c), b))
        candidates.append(combine(combine(b, a), c))
        candidates.append(combine(combine(b, c), a))
        candidates.append(combine(combine(c, a), b))
        candidates.append(combine(combine(c, b), a))

        candidates.sort()
        result = candidates[0]
        for c in candidates:
            if len(result) > len(c):
                result = c

        return result
