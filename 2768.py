class Solution:
    def countBlackBlocks(self, m: int, n: int, coordinates: List[List[int]]) -> List[int]:
        # number of black cells for each relevant block (revelant = at least one black cell)
        count = {}
        # fast lookup of known black cells
        black = set( ( x, y ) for x, y in coordinates)

        for x, y in coordinates:
            # each cell can be part of up to four blocks
            have = [ 0, 0, 0, 0 ]

            # those four blocks cover 9 cells
            # abc
            # def => x, y represent e
            # ghi
            a = ( x - 1, y - 1 ) in black
            b = ( x    , y - 1 ) in black
            c = ( x + 1, y - 1 ) in black
            d = ( x - 1, y     ) in black
            e = ( x    , y     ) in black
            f = ( x + 1, y     ) in black
            g = ( x - 1, y + 1 ) in black
            h = ( x    , y + 1 ) in black
            i = ( x + 1, y + 1 ) in black

            count[( x - 1, y - 1)] = a + b + d + e
            count[( x    , y - 1)] = b + c + e + f
            count[( x - 1, y    )] = d + e + g + h
            count[( x    , y    )] = e + f + h + i

        # initially only white cells
        total  = (m - 1) * (n - 1)
        result = [ total, 0, 0, 0, 0 ]

        # count blocks
        for (x, y), value in count.items():
            if 0 <= x < m - 1 and 0 <= y < n - 1:
                result[value] += 1 # one more "black" block
                result[0    ] -= 1 # one less "white" block

        return result
