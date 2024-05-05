class Solution:
    def shortestSubstrings(self, arr: List[str]) -> List[str]:
        all = defaultdict(int)

        # to save memory: use Python's hashes instead of the real strings

        for a in arr:
            size = len(a)
            for length in range(1, size + 1):
                me = set() # avoid substrings that occur more than once - but only within the same string
                for start in range(size - length + 1):
                    sub = a[start : start + length]
                    h   = hash(sub) & 0xFFFFFFFF

                    if h in me:
                        continue
                    me.add(h)

                    all[h] += 1

        # and again ...
        for a in arr:
            result = ""

            size = len(a)
            for length in range(1, size + 1):
                for start in range(size - length + 1):
                    sub = a[start : start + length]
                    h   = hash(sub) & 0xFFFFFFFF
                    # unique ?
                    if all[h] == 1:
                        result = min(result, sub) if result else sub

                if result:
                    break

            yield result
