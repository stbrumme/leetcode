class Solution:
    # breadth-first search, too slow for large numbers
    def bruteforce(self, n: int) -> int:
        dp    = set([ n ])
        steps = 0
        while True:
            next = set()
            for x in dp:
                if x <= 1:              # 0 => done
                    return steps + x    # 1 => done in next iteration

                # clear rightmost bit
                next.add(x ^ 1)

                # find rightmost set bit
                mask = 1
                while (x & mask) == 0:
                    mask <<= 1

                # clear its left neighbor
                mask <<= 1
                next.add(x ^ mask)

            dp     = next
            steps += 1

    def minimumOneBitOperations(self, n: int) -> int:
        # brute-forcing the problem for small numbers gives the sequence
        # 1, 3, 2, 7, 6, 4, 5, 15, 14, 12, 13, 8, 9, 10, 11, 31, 30, 28, 29, ...
        # which is part of OEIS: https://oeis.org/A006068
        # they even have a O(log2(n)) Python script to compute this sequence
        #for i in range(1, 20):
        #    print(i, self.bruteforce(i))

        # originally by Indranil Ghost / Joerg Arndt
        s = 1
        while True:
            shifted = n >> s
            if shifted == 0:
                break
            n ^= shifted
            s <<= 1
        return n
