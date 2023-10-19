class ATM:
    values = ( 500, 200, 100, 50, 20 )

    def __init__(self):
        self.stored = defaultdict(int)

    def deposit(self, banknotesCount: List[int]) -> None:
        for v in ATM.values:
            self.stored[v] += banknotesCount.pop() # reverse order

    def withdraw(self, amount: int) -> List[int]:
        backup = self.stored.copy()

        result = []
        for v in ATM.values: # largest denominations first
            pick = min(amount // v, self.stored[v]) # as many as many and available
            self.stored[v] -= pick
            amount         -= pick * v
            result.append(pick)

        # exact change
        if amount == 0:
            return reversed(result) # smallest denominations first

        # failed, don't dispense any cash
        self.stored = backup
        return [ -1 ]
