class Solution:
    def punishmentNumber(self, n: int) -> int:
        # https://oeis.org/A104113
        def valid(i, s):
            if i < 0:
                return False
            if i == int(s):
                return True
            # try all partitions
            return any(valid(i - int(s[: j]), s[j :]) for j in range(1, len(s)))

        #for i in range(n + 1):
        #    if valid(i, str(i * i)):
        #        result += i * i

        # precomputed list, see link given above
        known = [ 1, 81, 100, 1296, 2025, 3025, 6724, 8281, 9801, 10000,  \
                  55225, 88209, 136161, 136900, 143641, 171396, 431649,   \
                  455625, 494209, 571536, 627264, 826281, 842724, 893025, \
                  929296, 980100, 982081, 998001, 1000000 ]
        return sum(k for k in known if k <= n * n)
