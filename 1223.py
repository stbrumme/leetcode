class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        # roll 0...5 instead of 1...6 (zero-indexing) to simplify code

        modulo = 1_000_000_007

        # seed values: roll each number once
        have = []
        for i in range(6):
            have.append([ 1 ] + [ 0 ] * (rollMax[i] - 1))

        for _ in range(n - 1):
            each = [ sum(have[j]) % modulo for j in range(6) ]
            all  = sum(each)

            for i in range(6):
                # roll a different number (sum of all sequences not ending in current number)
                other = all - each[i]

                # prepend "other", discard the impossible value at index rollMax[i]
                have[i].insert(0, other)
                have[i].pop()

        return sum(sum(h) for h in have) % modulo
