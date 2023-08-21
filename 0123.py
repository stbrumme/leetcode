class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [ [ 0, None ]] # realized profit, ongoing transaction

        result = 0

        for current in prices:
            next = set()

            for check in dp:
                if check[1] == None:
                    next.add(tuple(check))
                    next.add(tuple([ check[0], current ])) # new TX
                    continue

                if check[1] >= current:
                    next.add(tuple([ check[0], current ])) # improved TX
                else:
                    next.add(tuple(check)) # keep it open
                    # and close it, too
                    gain = current - check[1]
                    if check[0] == 0:
                        next.add(tuple([ gain, None ])) # start second TX

                    total  = check[0] + gain
                    result = max(result, total)

            # prune: select best
            bestClosed = 0
            bestOpen0  = 0
            bestOpen1  = 0
            for check in next:
                if check[1] == None:
                    bestClosed = max(bestClosed, check[0])
                else:
                    potential = check[0] + current - check[1]
                    if check[0] == 0:
                        bestOpen0 = max(bestOpen0, potential)
                    else:
                        bestOpen1 = max(bestOpen1, potential)

            dp = set()
            dp.add(tuple([ 0, None ]))

            for check in next:
                if check[1] == None:
                    if check[0] == bestClosed:
                        dp.add(check)
                else:
                    potential = check[0] + current - check[1]
                    if check[0] == 0:
                        if potential == bestOpen0:
                            dp.add(check)
                    else:
                        if potential == bestOpen1:
                            dp.add(check)
                            bestOpen1 += 1 # skip if identical follow

        return result
