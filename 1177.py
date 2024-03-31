class Solution:
    def canMakePaliQueries(self, s: str, queries: List[List[int]]) -> List[bool]:
        # state encodes whether that letter is found an odd or even times
        state = 0
        have  = []
        for c in s:
            c = ord(c) - ord("a")
            state ^= 1 << c
            have.append(state)

        for left, right, k in queries:
            final = have[right]
            if left > 0:
                final ^= have[left - 1]

            odd = final.bit_count()
            yield odd <= 2*k + 1 # at most one letter may have an odd count
                                 # whenever replacing an "odd-count letter",
                                 # try to choose another "odd-count letter"
                                 # thus eliminating two  "odds"
