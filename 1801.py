class Solution:
    def getNumberOfBacklogOrders(self, orders: List[List[int]]) -> int:
        result = 0

        # basic order matching as done daily on every stock exchange worldwide
        # (and I work at one ...)
        bid = [] # max-heao, buy  orders
        ask = [] # min-heap, sell orders

        # we could combine orders on same price level but it doesn't matter for this problem
        for price, amount, type in orders:
            # update heaps with new order
            if type == 0:
                heappush(bid, [ -price, amount ])
            else:
                heappush(ask, [ +price, amount ])
            result += amount

            # find crossed orders or orders on same price level
            while bid and ask and -bid[0][0] >= ask[0][0]: # remember: bid is a max-heap
                # match as much as possible
                bidpx, bidsize = heappop(bid)
                askpx, asksize = heappop(ask)
                match = min(bidsize, asksize)

                # re-insert non-yet-matched size
                if bidsize > match:
                    heappush(bid, [ bidpx, bidsize - match ]) # price is already negative
                if asksize > match:
                    heappush(ask, [ askpx, asksize - match ])

                # matched on both sides of the orderbook
                result -= 2 * match

        return result % 1_000_000_007
