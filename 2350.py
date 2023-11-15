class Solution:
    def shortestSequence(self, rolls: List[int], k: int) -> int:
        # I had to read the problem discussion in order to understand what this problem is about ...
        # more or less they are asking for:
        # the length of the shortest sequence we cannot construct by taking elements from the array rolls
        result   = 1
        complete = 0

        # make a complete set of all dice sides
        freq = defaultdict(int)

        for r in rolls:
            # too much, skip it
            if freq[r] == result:
                continue

            # one more dice for our set
            freq[r]  += 1
            complete += 1
            # set is complete, extend length by one
            if complete == k:
                result  += 1
                complete = 0

        return result
