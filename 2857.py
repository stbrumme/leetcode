class Solution:
    def countPairs(self, coordinates: List[List[int]], k: int) -> int:
        result = 0

        # k = a  + b where
        # a = x1 ^ x2
        # b = y1 ^ y2
        # x1, y1, x2, y2 aren't negative, therefore a and b aren't negative, too
        # that means that
        # 0 <= a <= k as well as 0 <= b <= k

        # note: points don't need to be distinct
        seen = defaultdict(int)

        for x, y in coordinates:
            for a in range(k + 1):
                b = k - a

                # if a = x1 ^ x2 then a ^ x1 = x2
                # and of course       b ^ y1 = y2
                x2 = a ^ x
                y2 = b ^ y

                if ( x2, y2 ) in seen:
                    result += seen[ ( x2, y2 ) ]

            seen[ ( x, y ) ] += 1

        return result
