class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        # partial sums
        todo = [ 0 ] * (n + 1)
        todo[0] = 1

        for i in count(1):
            add = i ** x
            # too large, exit
            if add > n:
                break

            next = n
            while next >= add:
                # use current power
                todo[next] += todo[next - add]
                next -= 1

        return todo[n] % 1_000_000_007
