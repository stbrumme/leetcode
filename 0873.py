class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        result = 0
        lookup = set(arr)

        seen   = set() # basic cache: if (a, b) where already visited, then a longer chain exists

        # start with every possible pair a, b (where a < b)
        for i, a in enumerate(arr):
            for b in arr[i + 1 : ]:
                length = 2

                # keep going while one + two exists
                one = a
                two = b
                while one + two in lookup and ( one, two ) not in seen:
                    seen.add(( one, two ))
                    length  += 1
                    result   = max(result, length)
                    # prepare next step
                    one, two = two, one + two

        return result
