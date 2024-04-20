class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        # if we need "a" => "c" then sometimes it can be cheaper to convert "a" => "b", then "b" => "c"

        lookup = {}

        # direct mappings
        for have, need, dollars in zip(original, changed, cost):
            key = ( have, need )
            # in case there are several direct mappings "a" => "b" with different costs
            if key in lookup:
                lookup[key] = min(lookup[key], dollars)
            else:
                lookup[key] = dollars

        # indirect mappings
        abc = "abcdefghijklmnopqrstuvwxyz"
        again = True
        while again:
            again = False

            # Floyd-Warshall
            for a in abc:
                for b in abc:
                    if ( a, b ) in lookup:
                        cost1 = lookup[( a, b )]
                        for c in abc:
                            if a != c and ( b, c ) in lookup:
                                cost2 = lookup[( b, c )]
                                total = cost1 + cost2
                                key   = ( a, c )
                                if key not in lookup or total < lookup[key]:
                                    # new or cheaper mapping
                                    lookup[key] = total
                                    again = True

        # convert
        result = 0
        for s, t in zip(source, target):
            # no mapping needed
            if s == t:
                continue

            key = ( s, t )

            # check mapping
            if key not in lookup:
                return -1

            result += lookup[key]

        return result
