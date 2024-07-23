class Solution:
    def minLengthAfterRemovals(self, nums: List[int]) -> int:
        # there can be duplicates but we can't remove them pairwise
        # thus try to remove the most frequent numbers first
        size = len(nums)

        freq = defaultdict(int)
        for n in nums:
            freq[n] += 1

        # max-heap
        todo = [ -v for v in freq.values() ]
        heapify(todo)
        print(todo)

        high  = -todo[0]
        other = size - high
        if high > other:
            # can't get rid of all values because the most frequent number
            # can't be paired with itself
            return high - other

        while len(todo) >= 2:
            # pair the most frequent values
            one = heappop(todo) + 1 # reduce by 1, but it's negated anyway

            two = todo[0]       + 1 # heapreplace instead of heappop + heappush is faster
            if two != 0:
                heapreplace(todo, two)
            else:
                heappop    (todo)   # remove two, it's zero

            if one != 0:
                heappush(todo, one)

        return len(todo) # 0 or 1
