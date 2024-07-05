class Solution:
    def valueAfterKSeconds(self, n: int, k: int) -> int:
        # brute force but there should be a mathematical solution, too
        modulo = 1_000_000_007
        have   = [ 1 ] * n
        for _ in range(k):
            next = [ have[0] ]
            for h in have[1 :]:
                next.append(next[-1] + h)
            have = next

            # keep numbers small
            if _ & 7 == 0:
                for i in range(20, n):
                    have[i] %= modulo

        return have[-1] % modulo
