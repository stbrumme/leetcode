class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        tx = defaultdict(list)
        # extract fields
        for i, t in enumerate(transactions):
            name, time, amount, city = t.split(",")
            tx[name].append(( int(time), int(amount), city, i, t ))

        invalid = [ False ] * len(transactions)

        for name in tx:
            tx[name].sort()

            for i, (time, amount, city, id, t) in enumerate(tx[name]):
                if amount > 1000:
                    invalid[id] = True

                for j in range(i + 1, len(tx[name])):
                    time2, amount2, city2, id2, t2 = tx[name][j]
                    if time2 - time > 60:
                        break
                    if city2 != city:
                        # flag both transactions
                        invalid[id]  = True
                        invalid[id2] = True

        return [ t for i, t in enumerate(transactions) if invalid[i] ]
