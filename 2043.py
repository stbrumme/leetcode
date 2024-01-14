class Bank:
    def __init__(self, balance: List[int]):
        self.size = len(balance) # = n
        self.balance = [ 0 ] + balance

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if 1 <= account1 <= self.size and 1 <= account2 <= self.size: # and account1 != account2:
            if self.balance[account1] >= money:
                self.balance[account1] -= money
                self.balance[account2] += money
                return True
        return False

    def deposit(self, account: int, money: int) -> bool:
        if 1 <= account <= self.size:
            self.balance[account] += money
            return True
        return False

    def withdraw(self, account: int, money: int) -> bool:
        if 1 <= account <= self.size:
            if self.balance[account] >= money:
                self.balance[account] -= money
                return True
        return False
