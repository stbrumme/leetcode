class Solution:
    def reinitializePermutation(self, n: int) -> int:
        # https://oeis.org/A002326
        # just brute force
        need = list(range(n))
        have = need.copy()

        step = 0
        while have != need or step == 0:
            next = []
            for i, h in enumerate(have):
                if i & 1:
                    index = n // 2 + (i - 1) // 2
                else:
                    index = i // 2

                next.append(have[index])

            have  = next
            step += 1

        return step
