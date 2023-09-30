class ProductOfNumbers:
    def __init__(self):
        self.data = []

    def add(self, num: int) -> None:
        self.data.append(num)

    def getProduct(self, k: int) -> int:
        return prod(self.data[-k:])
