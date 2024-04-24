class Solution:
    def oddEvenJumps(self, arr: List[int]) -> int:
        size = len(arr)

        # find next higher index (for odd jumps)
        high = [ None ] * size
        stack = []
        for a, i in sorted( ( a, i ) for i, a in enumerate(arr)):
            while stack and stack[-1] < i:
                high[stack.pop()] = i
            stack.append(i)

        # find next lower index (for even jumps)
        low = [ None ] * size
        stack = []
        for a, i in sorted( ( -a, i ) for i, a in enumerate(arr)):
            while stack and stack[-1] < i:
                low[stack.pop()] = i
            stack.append(i)

        print(high)
        print(low)

        @cache
        def deeper(pos, isOdd):
            if pos == size - 1:
                return 1 # reached end
            if pos == None:
                return 0 # impossible to finish

            # next jump
            if isOdd:
                return deeper(high[pos], False)
            else:
                return deeper(low [pos], True)

        return sum([ deeper(i, True) for i in range(size) ])
