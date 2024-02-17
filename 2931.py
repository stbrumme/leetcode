class Solution:
    def maxSpending(self, values: List[List[int]]) -> int:
        result = 0

        # buy cheap things first (when day is a small number)
        todo = [] # min-heap
        for i, shop in enumerate(values):
            heappush(todo, ( shop.pop(), i ))

        day = 1
        while todo:
            price, shop = heappop(todo)
            result += day * price
            day    += 1

            if values[shop]:
                heappush(todo, ( values[shop].pop(), shop ))

        return result
