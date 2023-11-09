class Cashier:
    def __init__(self, n: int, discount: int, products: List[int], prices: List[int]):
        self.items    = { pro : pri for pro, pri in zip(products, prices) }
        self.discount = (100 - discount) / 100
        self.trigger  = n
        self.people   = 0

    def getBill(self, product: List[int], amount: List[int]) -> float:
        cost = sum( self.items[p] * a for p, a in zip(product, amount) )
        self.people += 1
        if self.people == self.trigger:
            self.people = 0
            cost *= self.discount

        return cost
