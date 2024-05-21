class Solution:
    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
        size = len(price)

        # remove items which are for free
        for i in range(size):
            if price[i] == 0:
                needs[i] = 0

        # everything's for free
        needs = tuple(needs)
        if sum(needs) == 0:
            return 0

        # worst case: ignore all offers and pay full price
        limit = 0
        for p, n in zip(price, needs):
            limit += p * n

        # treat standard price as an offer of a single item
        for i in range(size):
            single    = [ 0 ] * size
            single[i] = 1
            special.append(single + [ price[i] ])

        # consider only offers which don't exceed the number of needed items
        offers = {}
        valid  = [ s for s in special if all( h <= n for h, n in zip(s, needs) ) ]
        for v in valid:
            items = tuple(v[ : -1])
            cost  = v[-1]
            if offers.get(items, +inf) > cost:
                offers[items] = cost

        todo = [ (0, needs) ]      # ( price paid so far, items still needed )
        seen = { needs: 0 }
        while True:
            cost, have = heappop(todo)

            # found lowest price
            if sum(have) == 0: # have == [ 0,0,0,... ]
                return cost

            # double-check that we haven't already processed it
            if seen[have] < cost:
                continue

            # try every offer
            for o in offers:
                total = cost + offers[o]
                if total > limit: # too expensive
                    continue

                next = [ h - oo for h, oo in zip(have, o) ]
                if min(next) >= 0: # must not buy more than needed
                    # ensure we haven't seen a better price
                    next = tuple(next)
                    if total < seen.get(next, +inf):
                        heappush(todo, ( total, next ))
                        seen[next] = total

                        # potential solution
                        if sum(next) == 0:
                            limit = total
