class Solution:
    def colorTheGrid(self, m: int, n: int) -> int:
        modulo = 1_000_000_007

        # let's assume m represents the number of columns, n the number of rows
        # m <= 5, that means at most 3^5 = 243 combinations per row
        limit  = 3 ** m

        # precalculate all valid rows, that number is much lower:
        # m = 1 ... 5 => [ 3, 6, 12, 24, 48 ]
        single = []
        for i in range(limit):
            okay = True
            # compare two cells, avoid same color
            a = i
            b = i // 3
            for _ in range(m - 1):
                #
                if a % 3 == b % 3:
                    okay = False
                    break
                a   = b
                b //= 3

            if okay:
                single.append(i)

        # now all valid combinations of two rows
        allowed = defaultdict(list)
        for one in single:
            for two in single:
                okay = True
                a = one
                b = two
                for _ in range(m):
                    if a % 3 == b % 3:
                        okay = False
                        break
                    a //= 3
                    b //= 3

                if okay:
                    allowed[one].append(two)

        @cache
        def deeper(pos, code):
            return 1 if pos == n else sum(deeper(pos + 1, next) for next in allowed[code]) % modulo

        return sum(deeper(1, initial) for initial in allowed) % modulo
