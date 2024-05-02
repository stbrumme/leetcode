class Solution:
    def squareFreeSubsets(self, nums: List[int]) -> int:
        modulo = 1_000_000_007

        # version B: 110 ms, 17.6 MB
        result = 0

        # count numbers
        freq = [ 0 ] * (30 + 1)
        for n in nums:
            freq[n] += 1

        # special case: each 1 may be part of every set
        freq[1] = pow(2, freq[1], modulo) - 1

        # create all eligible sets
        todo = [ () ]
        for i in range(1, len(freq)):
            # skip if it isn't part of the input data
            if freq[i] == 0:
                continue
            # skip basic squares
            if i % 4 == 0 or i % 9 == 0 or i == 16 or i == 25:
                continue

            # append current number to each set
            next = todo.copy()
            for one in todo:
                square = False
                count  = freq[i]
                for o in one:
                    # if gcd is greater than one then there will be a square
                    if gcd(i, o) > 1:
                        square = True
                        break

                    count *= freq[o]

                if not square:
                    # valid, accept it
                    next.append(one + (i, ))
                    result += count

            todo    = next
            result %= modulo

        return result

        # version A: 4326 ms, 696 MB

        # basic squares and their multiples: 4, 8, 9, 12, 16, 18, 20, 24, 25, 27
        squares = set()
        for s in range(2, 30 + 1):
            for t in range(s*s, 30 + 1, s*s):
                squares.add(t)

        # remove those squares (and their multiples)
        candidates = [ n for n in nums if n not in squares ]
        if not candidates:
            return 0
        size = len(candidates)
        high = max(candidates)

        # precompute multiples and prime factors
        block = [ 0 ] * (high + 1) # 0 isn't used, 1 is square-free and allowed multiple times
        for i in range(2, high + 1):
            for j in range(2, high + 1):
                if gcd(i, j) != 1:
                    block[i] |= 1 << j

        @lru_cache(maxsize = 200_000)
        def deeper(pos, disallowed):
            # found a new set
            if pos == size:
                return 1

            # skip current number
            found = deeper(pos + 1, disallowed)

            # use  current number
            n    = candidates[pos]
            mask = 1 << n
            if not (mask & disallowed):
                found += deeper(pos + 1, disallowed | block[n])

            return found % modulo

        return (deeper(0, 0) - 1) % modulo # ignore empty set
