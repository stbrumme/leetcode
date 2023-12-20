class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        # precompute how to add to digits
        odd = {} # old digit => new digit after adding a with modulo
        for i in range(10):
            odd[str(i)] = str((i + a) % 10)

        seen = set()
        def deeper(x):
            # caching
            if x in seen:
                return
            seen.add(x)

            # rotate
            deeper(x[-b:] + x[:-b])
            # shift
            for i in range(1, len(x), 2): # only odd indices ...
                                          # careful reading the problem statement would have saved me 10 minutes :-()
                x = x[:i] + odd[x[i]] + x[i+1:]
            deeper(x)

        deeper(s)
        return min(seen)
