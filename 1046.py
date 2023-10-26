class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # all those minus-signs for the max-heap make the code look ugly ...
        for i in range(len(stones)):
            stones[i] = -stones[i]
        heapify(stones)

        while len(stones) > 1:
            y = -heappop(stones)
            x = -heappop(stones)
            if x != y:
                heappush(stones, -(y - x))
        return -stones[0] if stones else 0
