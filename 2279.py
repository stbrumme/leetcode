class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        need = [] # min-heap
        for c, r in zip(capacity, rocks):
            heappush(need, c - r)

        result = 0
        while need and additionalRocks >= 0:
            next = heappop(need)
            additionalRocks -= next
            if additionalRocks >= 0:
                result += 1

        return result
